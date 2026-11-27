"""Script đào dữ liệu hành vi thật trên bộ data/preclass/ của BTC.

Cách chạy:
    python evidence/count_preclass.py <duong_dan_toi_thu_muc_data_preclass>

Chỉ dùng thư viện chuẩn của Python. Không sửa dữ liệu gốc; không giải ẩn danh học viên.
Mọi con số đều in rõ x/N, % và định nghĩa mẫu số để người khác chạy lại ra đúng kết quả.
"""
import csv
import json
import os
import sys
from collections import Counter, defaultdict


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def pct(x, n):
    return (100.0 * x / n) if n else 0.0


def fmt(x, n):
    return f"{x}/{n} ({pct(x, n):.1f}%)"


def safe_json(s):
    if not s:
        return {}
    try:
        return json.loads(s)
    except Exception:
        return {}


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python evidence/count_preclass.py <thu_muc_data_preclass>")
        sys.exit(1)

    base = sys.argv[1]
    learners = read_csv(os.path.join(base, "learners.csv"))
    answers = read_csv(os.path.join(base, "answers.csv"))
    chat = read_csv(os.path.join(base, "chat.csv"))
    class_events = read_csv(os.path.join(base, "class_events.csv"))
    rewards = read_csv(os.path.join(base, "rewards.csv"))
    completed = read_csv(os.path.join(base, "completed_items.csv"))

    # Đọc events.csv dạng stream vì file ~26MB
    active_learners = set()
    event_counts = Counter()
    quiz_opened_hv = set()
    quiz_dismissed_total = 0
    quiz_dismissed_skipped = 0
    quiz_skipped_hv = set()
    seek_total = 0
    seek_crossed_stop = 0
    seek_crossed_hv = set()
    agent_shown_total = 0
    agent_shown_hv = set()
    so_hieu_bai_opened = 0
    so_hieu_bai_reviewed = 0
    video_quiz_examples = []
    skipped_examples = []
    agent_shown_per_hv = Counter()
    sessions_per_hv = Counter()
    lectures_per_hv = Counter()

    events_path = os.path.join(base, "events.csv")
    with open(events_path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            t = row["type"]
            hv = row["hv"]
            event_counts[t] += 1
            if hv:
                active_learners.add(hv)
            if t == "session_started" and hv:
                sessions_per_hv[hv] += 1
            elif t == "lecture_opened" and hv:
                lectures_per_hv[hv] += 1
            elif t == "quiz_item_opened":
                if hv:
                    quiz_opened_hv.add(hv)
            elif t == "quiz_item_dismissed":
                quiz_dismissed_total += 1
                d = safe_json(row["data"])
                if d.get("skipped_stop") is True:
                    quiz_dismissed_skipped += 1
                    if hv:
                        quiz_skipped_hv.add(hv)
                    if len(skipped_examples) < 5:
                        skipped_examples.append((hv, row["video"], d.get("question_id"), row["occurred_at"]))
            elif t == "video_seeked":
                seek_total += 1
                d = safe_json(row["data"])
                if d.get("crossed_stop") is True:
                    seek_crossed_stop += 1
                    if hv:
                        seek_crossed_hv.add(hv)
            elif t == "agent_message_shown":
                agent_shown_total += 1
                if hv:
                    agent_shown_hv.add(hv)
                    agent_shown_per_hv[hv] += 1
            elif t == "so_hieu_bai_opened":
                so_hieu_bai_opened += 1
            elif t == "so_hieu_bai_reviewed":
                so_hieu_bai_reviewed += 1

    print("=" * 70)
    print("1. QUY MO HOAT DONG")
    print("=" * 70)
    print(f"Tong tai khoan learners.csv: {len(learners)}")
    print(f"Hoc vien co hoat dong trong events.csv: {fmt(len(active_learners), len(learners))}")
    print(f"Tong dong events.csv: {sum(event_counts.values())}")
    print(f"Tong dong completed_items.csv: {len(completed)}")

    print("\n" + "=" * 70)
    print("2. BO QUA CAU HOI GIUA VIDEO (events.csv)")
    print("=" * 70)
    print(f"quiz_item_opened: {event_counts['quiz_item_opened']} luot ({len(quiz_opened_hv)} hoc vien)")
    print(f"quiz_item_dismissed (skipped_stop=true / tong dismissed): {fmt(quiz_dismissed_skipped, quiz_dismissed_total)}")
    print(f"quiz_item_dismissed (skipped_stop=true / tong quiz_item_opened): {fmt(quiz_dismissed_skipped, event_counts['quiz_item_opened'])}")
    print(f"Hoc vien tung bo qua it nhat 1 quiz / hoc vien tung mo quiz: {fmt(len(quiz_skipped_hv), len(quiz_opened_hv))}")
    print(f"video_seeked qua moc cau hoi (crossed_stop=true / tong seek): {fmt(seek_crossed_stop, seek_total)} ({len(seek_crossed_hv)} hoc vien)")
    print(f"so_hieu_bai_reviewed / so_hieu_bai_opened: {fmt(so_hieu_bai_reviewed, so_hieu_bai_opened)}")

    print("\n" + "=" * 70)
    print("3. TRA LOI CAU HOI & TU GIAI THICH (answers.csv)")
    print("=" * 70)
    nguon_counts = Counter(r["nguon"] for r in answers)
    print("Phan bo theo nguon:", dict(nguon_counts))

    for src in ("video_quiz", "pre_post_post", "thuc_hanh"):
        rows_l1 = [r for r in answers if r["nguon"] == src and r["lan_thu"] == "1" and r["was_correct"] in ("True", "False")]
        wrong_l1 = [r for r in rows_l1 if r["was_correct"] == "False"]
        hv_l1 = {r["hv"] for r in rows_l1}
        hv_wrong = {r["hv"] for r in wrong_l1}
        print(f"  [{src}] Sai lan 1 (lan_thu=1): {fmt(len(wrong_l1), len(rows_l1))} | HV tung sai lan 1: {fmt(len(hv_wrong), len(hv_l1))}")
        if src == "video_quiz":
            # Kiem tra xem nhung (hv, ref) sai lan 1 co lan_thu >= 2 khong, va co sua dung khong
            attempts_by_key = defaultdict(list)
            for r in answers:
                if r["nguon"] == "video_quiz":
                    attempts_by_key[(r["hv"], r["ref"])].append(r)
            wrong_keys = {(r["hv"], r["ref"]) for r in wrong_l1}
            retried = 0
            retried_correct = 0
            for k in wrong_keys:
                atts = attempts_by_key[k]
                later = [a for a in atts if int(a["lan_thu"] or 0) >= 2]
                if later:
                    retried += 1
                    if any(a["was_correct"] == "True" for a in later):
                        retried_correct += 1
            print(f"  [video_quiz] Sau khi sai lan 1, KHONG lam lai: {fmt(len(wrong_keys) - retried, len(wrong_keys))}")
            print(f"  [video_quiz] Sau khi sai lan 1, co lam lai va dung: {fmt(retried_correct, len(wrong_keys))}")
            video_quiz_examples = wrong_l1[:5]

    # Tu giai thich & rubric chat
    gt_rows = [r for r in answers if r["nguon"] == "giai_thich"]
    gt_hv = {r["hv"] for r in gt_rows}
    print(f"  [giai_thich] Tong luot tu giai thich: {len(gt_rows)} ({len(gt_hv)} hoc vien / {len(active_learners)} HV hoat dong = {pct(len(gt_hv), len(active_learners)):.1f}%)")
    chat_ans = [r for r in answers if r["nguon"] == "chat"]
    chat_scored = [r for r in chat_ans if r["trang_thai_cham"] == "da_cham"]
    y_moi_0 = [r for r in chat_scored if r["rubric_y_moi"] == "0"]
    y_moi_2 = [r for r in chat_scored if r["rubric_y_moi"] == "2"]
    bam_bai_0 = [r for r in chat_scored if r["rubric_bam_bai"] == "0"]
    print(f"  [answers nguon=chat da_cham] {len(chat_scored)}/{len(chat_ans)}")
    print(f"    rubric_y_moi == 0 (chua co y rieng): {fmt(len(y_moi_0), len(chat_scored))}")
    print(f"    rubric_y_moi == 2 (co phan bien/vi du rieng): {fmt(len(y_moi_2), len(chat_scored))}")
    print(f"    rubric_bam_bai == 0 (khong bam bai): {fmt(len(bam_bai_0), len(chat_scored))}")

    print("\n" + "=" * 70)
    print("4. LOP HOC AI & BAN HOC AI XEN VAO (class_events, events, chat, rewards)")
    print("=" * 70)
    dir_rows = [r for r in class_events if r["type"] == "director_decided"]
    dir_inserted = []
    int_types = Counter()
    classmates = Counter()
    for r in dir_rows:
        d = safe_json(r["data"])
        if d.get("inserted") is True:
            dir_inserted.append(r)
            int_types[d.get("intervention_type", "")] += 1
            classmates[d.get("classmate_id", "")] += 1
    print(f"director_decided inserted=true / tong quyet dinh: {fmt(len(dir_inserted), len(dir_rows))}")
    print("  Theo classmate_id:", dict(classmates))
    print("  Theo intervention_type:", dict(int_types))

    chat_channels = Counter(r["channel"] for r in chat)
    chat_kinds = Counter(r["kind"] for r in chat)
    chat_agents = Counter(r["agent_id"] for r in chat)
    chat_with_int = [r for r in chat if r["intervention_id"]]
    disc_replies = [r for r in chat if r["channel"] == "video_discussion_reply"]
    real_replies_ans = [r for r in answers if r["la_reply_that"] == "True"]
    disc_reply_hv = {r["hv"] for r in disc_replies}
    print(f"agent_message_shown (ban hoc AI xen vao hien ra): {agent_shown_total} luot tren {len(agent_shown_hv)} hoc vien")
    print(f"chat.csv tong luot: {len(chat)} | theo channel: {dict(chat_channels)}")
    print(f"  theo kind: {dict(chat_kinds)}")
    print(f"  theo agent_id: {dict(chat_agents)}")
    print(f"Luot HV nhan trong video_discussion_reply / agent_message_shown: {fmt(len(disc_replies), agent_shown_total)}")
    print(f"Luot chat gan intervention_id / agent_message_shown: {fmt(len(chat_with_int), agent_shown_total)}")
    print(f"HV tung reply trong video_discussion_reply / HV thay agent_message_shown: {fmt(len(disc_reply_hv), len(agent_shown_hv))}")
    print(f"answers.csv co la_reply_that=True: {len(real_replies_ans)}")

    rew_types = Counter(r["hanh_vi"] for r in rewards)
    rew_hv = {r["hv"] for r in rewards}
    print(f"rewards.csv tong: {len(rewards)} ({len(rew_hv)} HV) | theo hanh_vi: {dict(rew_types)}")

    print("\n" + "=" * 70)
    print("5. PHAN NHOM TAN SUAT HOC VIEN (cho persona chi phi)")
    print("=" * 70)
    quiz_per_hv = Counter(r["hv"] for r in answers if r["nguon"] in ("video_quiz", "pre_post_post", "thuc_hanh"))
    # Phan bo so phien / HV trong 21 ngay (05/11 -> 25/11)
    active_list = sorted(active_learners)
    sess_vals = sorted(sessions_per_hv.get(hv, 0) for hv in active_list)
    low = sum(1 for v in sess_vals if v <= 1)
    mid = sum(1 for v in sess_vals if 2 <= v <= 4)
    high = sum(1 for v in sess_vals if v >= 5)
    print(f"Trong {len(active_list)} HV hoat dong (21 ngay 05/11-25/11), so phien session_started:")
    print(f"  Dung it (0-1 phien): {fmt(low, len(active_list))}")
    print(f"  Dung vua (2-4 phien): {fmt(mid, len(active_list))}")
    print(f"  Dung nhieu (>=5 phien): {fmt(high, len(active_list))}")
    if sess_vals:
        print(f"  Trung binh: {sum(sess_vals)/len(sess_vals):.2f} phien/HV | Trung vi: {sess_vals[len(sess_vals)//2]} | Max: {sess_vals[-1]}")

    quiz_vals = sorted(quiz_per_hv.get(hv, 0) for hv in active_list)
    print(f"So luot tra loi (video_quiz+pre_post+thuc_hanh) / HV hoat dong: TB {sum(quiz_vals)/len(quiz_vals):.2f} | Max {quiz_vals[-1]}")
    shown_vals = sorted(agent_shown_per_hv.get(hv, 0) for hv in agent_shown_hv)
    if shown_vals:
        print(f"So luot agent_message_shown / HV thay ban hoc AI: TB {sum(shown_vals)/len(shown_vals):.1f} | Trung vi {shown_vals[len(shown_vals)//2]} | Max {shown_vals[-1]}")

    print("\n" + "=" * 70)
    print("6. VI DU AN DANH CU THE")
    print("=" * 70)
    print("-- 5 vi du bo qua quiz giua video (skipped_stop=true):")
    for ex in skipped_examples:
        print("  ", ex)
    print("-- 5 vi du tra loi video_quiz sai lan 1:")
    for r in video_quiz_examples:
        print(f"   id={r['id']} hv={r['hv']} lesson={r['lesson_id']} kc={r['kc_code']} ref={r['ref']} at={r['created_at']}")
    print("-- 5 vi du chat voi ban hoc AI (video_discussion_reply):")
    for r in disc_replies[:5]:
        print(f"   id={r['id']} hv={r['hv']} agent={r['agent_id']} int={r['intervention_id']} len_q={r['do_dai_cau_hoi']} len_a={r['do_dai_tra_loi']} at={r['asked_at']}")


if __name__ == "__main__":
    main()
