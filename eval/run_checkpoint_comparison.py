"""Phát lại benchmark CP2 trên main và nhánh hiện tại để kiểm tương thích."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
from threading import local
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "eval" / "benchmark.csv"
LABEL = re.compile(r"^\[([^\]]+)\]")
CITATION = re.compile(r"\[D\d{2}-P\d{2}\]")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def replay(source, workers):
    sys.path.insert(0, str(source / "codebase"))
    import agent
    import ai

    if ai.MODEL_PROVIDER == "fake":
        raise RuntimeError("Cần model thật cho phép đối chiếu.")
    usage = local()

    def measured_model(system, user):
        result = ai.call_model(system, user)
        usage.calls.append({key: result[key] for key in ("tokens_in", "tokens_out")})
        return result

    def run_case(case):
        usage.calls = []
        error = None
        try:
            output = agent.answer(case["input"])["output"]
        except (OSError, RuntimeError, ValueError) as failure:
            output, error = "", type(failure).__name__
        label = LABEL.match(output)
        return {
            "id": case["id"],
            "label": label.group(1) if label else None,
            "citations": sorted(set(CITATION.findall(output))),
            "response": output,
            "error": error,
            "model_calls": usage.calls,
        }

    with BENCHMARK.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    with patch.object(agent, "call_model", measured_model), ThreadPoolExecutor(workers) as pool:
        return {"model": ai.MODEL_NAME, "cases": list(pool.map(run_case, rows))}


def compare(baseline_ref, workers):
    # Nạp cấu hình hiện có một lần để hai tiến trình con nhận cùng cấu hình.
    sys.path.insert(0, str(ROOT / "codebase"))
    import ai

    baseline = git("rev-parse", baseline_ref).decode().strip()
    with TemporaryDirectory() as target:
        archive = git("archive", baseline, "codebase", "data")
        subprocess.run(["tar", "-xf", "-", "-C", target], input=archive, check=True)
        results = {}
        for key, source in (("main", Path(target)), ("cp4", ROOT)):
            command = [
                sys.executable, str(Path(__file__).resolve()),
                "--worker", str(source), "--workers", str(workers),
            ]
            results[key] = json.loads(subprocess.check_output(command))
            print(f'Đã phát lại {len(results[key]["cases"])} ca cho {key}.', flush=True)

    if any(result["model"] != ai.MODEL_NAME for result in results.values()):
        raise ValueError("Model giữa hai bản chạy không khớp.")
    return {
        "baseline_revision": baseline,
        "cp4_revision": git("rev-parse", "HEAD").decode().strip(),
        "benchmark_sha256": hashlib.sha256(BENCHMARK.read_bytes()).hexdigest(),
        **results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", default="main")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--worker", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.worker is not None:
        print(json.dumps(replay(args.worker, args.workers), ensure_ascii=False))
        return
    if args.output is None or args.output.exists():
        parser.error("Chọn một đường dẫn --output mới.")
    result = compare(args.baseline, args.workers)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


if __name__ == "__main__":
    main()
