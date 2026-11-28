"""Đánh giá cách diễn đạt và lượt hội thoại của phiên dạy lại."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DATASET = Path(__file__).with_name("teachback-variants.json")
sys.path.insert(0, str(ROOT / "codebase"))

import ai
from teachback import TeachbackSession
from tools import LESSONS_PATH, load_days

LABELS = {None, "ĐỦ Ý", "THIẾU Ý", "HIỂU SAI"}
EXPLANATIONS = {"advance", "ask", "redirect", "refuse", "review"}
COMMANDS = {"review": "review", "skip": "deferred", "stop": "unchecked"}


def load_cases(by_code):
    cases = json.loads(DATASET.read_text(encoding="utf-8"))["cases"]
    if len({case["id"] for case in cases}) != len(cases):
        raise ValueError("ID ca bị trùng.")
    if {case["lesson"] for case in cases} != by_code.keys():
        raise ValueError("Bộ ca cần phủ đúng các mục hiện có.")
    for case in cases:
        _, item = by_code[case["lesson"]]
        turns = case["turns"]
        if not turns:
            raise ValueError(f'{case["id"]} chưa có lượt.')
        for i, turn in enumerate(turns):
            action, expected = turn["action"], turn["expect"]
            allowed = EXPLANATIONS if action == "explain" else {COMMANDS.get(action)}
            if expected not in allowed or turn["label"] not in LABELS:
                raise ValueError(f'{case["id"]} có kỳ vọng hoặc nhãn chưa hợp lệ.')
            if action == "explain" and not turn.get("text", "").strip():
                raise ValueError(f'{case["id"]} chưa có lời giảng.')
            if expected in ("advance", "deferred", "unchecked") and i < len(turns) - 1:
                raise ValueError(f'{case["id"]} có lượt sau khi đã chốt.')
            if "focus" in turn and (
                expected != "ask" or not 1 <= turn["focus"] <= len(item["checkpoints"])
            ):
                raise ValueError(f'{case["id"]} có trọng tâm ngoài mục đang ôn.')
    return cases


def observe(session, turn, model):
    action = turn["action"]
    if action == "review":
        return "review", None, session.reveal()
    if action == "skip":
        session.skip()
        return "deferred", None, ""
    if action == "stop":
        return "unchecked", None, ""

    response = session.explain(turn["text"], model)
    label = session.last_label
    if session.current is None:
        outcome = "advance" if label == "ĐỦ Ý" else "deferred"
    elif response.startswith("Giám khảo · "):
        outcome = "review"
    elif response.startswith("AI người học · "):
        outcome = "ask" if label else "redirect"
    elif response.startswith("Phiên này dùng để dạy lại"):
        outcome = "refuse"
    else:
        outcome = "unknown"
    return outcome, label, response


def run_case(case, by_code):
    day, item = by_code[case["lesson"]]
    session = TeachbackSession({**day, "items": [item]})
    results = []
    usage = []
    finished = False

    def measured_model(system, user):
        reply = ai.call_model(system, user)
        usage.append({key: reply[key] for key in ("tokens_in", "tokens_out")})
        return reply

    for i, turn in enumerate(case["turns"], 1):
        before = len(usage)
        observed = {"turn": i, "pass": False}
        if finished:
            observed["outcome"] = "not_reached"
            results.append(observed)
            continue

        try:
            outcome, label, response = observe(session, turn, measured_model)
            failures = []
            if outcome != turn["expect"]:
                failures.append("outcome")
            if label != turn["label"]:
                failures.append("label")
            if outcome in ("ask", "redirect") and response.count("?") != 1:
                failures.append("question_count")
            if "focus" in turn:
                question = item["checkpoints"][turn["focus"] - 1]["question"]
                if response != "AI người học · " + question:
                    failures.append("focus")
            if outcome in ("advance", "review") and (
                f'[{item["code"]}]' not in response or day["source"] not in response
            ):
                failures.append("source")
            if (turn["action"] != "explain" or turn["expect"] == "refuse") and len(usage) != before:
                failures.append("unexpected_model_call")
            if turn["expect"] == "unchecked" and session.statuses[0] != "Chưa kiểm tra":
                failures.append("status")
            observed.update(
                outcome=outcome, label=label, response=response, failures=failures,
                status=session.statuses[0], hints=session.hints,
            )
            observed["pass"] = not failures
            finished = session.current is None or turn["action"] == "stop"
        except (OSError, RuntimeError, ValueError) as error:
            observed.update(outcome="error", error=type(error).__name__)
            finished = True
        observed["model_calls"] = len(usage) - before
        results.append(observed)

    return {
        "id": case["id"], "style": case["style"], "lesson": case["lesson"],
        "pass": all(turn["pass"] for turn in results), "turns": results, "usage": usage,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    by_code = {
        item["code"]: (day, item)
        for day in load_days() for item in day["items"]
    }
    cases = load_cases(by_code)
    print(f'{len(cases)} ca, {sum(len(c["turns"]) for c in cases)} lượt, {len(by_code)} mục.')
    if args.validate_only:
        print(dict(Counter(case["style"] for case in cases)))
        return
    if args.output is None or args.output.exists() or ai.MODEL_PROVIDER == "fake":
        parser.error("Cần model thật và đường dẫn --output mới.")
    with ThreadPoolExecutor(args.workers) as pool:
        results = list(pool.map(lambda case: run_case(case, by_code), cases))
    payload = {
        "model": ai.MODEL_NAME,
        "revision": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip(),
        "dataset_sha256": hashlib.sha256(DATASET.read_bytes()).hexdigest(),
        "lessons_sha256": hashlib.sha256(LESSONS_PATH.read_bytes()).hexdigest(),
        "cases": results,
    }
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(f'{sum(case["pass"] for case in results)}/{len(results)} ca đạt.')


if __name__ == "__main__":
    main()
