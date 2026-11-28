"""Kiểm ranh giới giữa câu hỏi và đáp án, cùng chuyển trạng thái phiên ôn."""

import json
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codebase"))

from teachback import TeachbackSession
from tools import load_days


def verdict(*points, relevant=True):
    states = {"đúng": "correct", "thiếu": "missing", "sai": "incorrect"}
    return {"text": json.dumps({"relevant": relevant, "points": {
        str(i): states[point] for i, point in enumerate(points, 1)
    }})}


class TeachbackTest(unittest.TestCase):
    def setUp(self):
        self.days = load_days()
        self.session = TeachbackSession(self.days[0])

    def test_can_choose_each_day(self):
        self.assertEqual(len(self.days), 15)
        self.assertEqual(sum(len(day["items"]) for day in self.days), 52)

    def test_learner_receives_questions_without_judge_answers(self):
        model = Mock(side_effect=[verdict("sai", "sai"), {"text": "2"}])
        item = self.session.current
        text = self.session.explain("Mọi AI đều là LLM, kể cả bộ lọc thư.", model)

        self.assertEqual(text, "AI người học · " + item["checkpoints"][1]["question"])
        request = json.loads(model.call_args_list[1].args[1])
        self.assertEqual(set(request), {"loi_moi_nhat", "cau_hoi"})
        for point in item["checkpoints"]:
            self.assertNotIn(point["answer"], text)
            self.assertNotIn(point["answer"], model.call_args_list[1].args[1])
        self.assertEqual(self.session.index, 0)

    def test_wrong_point_takes_priority_then_asks_missing_point(self):
        model = Mock(side_effect=[verdict("thiếu", "sai"), verdict("thiếu", "đúng")])
        item = self.session.current

        first = self.session.explain("Công cụ tạo ảnh cũng là LLM.", model)
        second = self.session.explain("GenAI tạo ảnh, LLM chuyên ngôn ngữ.", model)

        self.assertIn(item["checkpoints"][1]["question"], first)
        self.assertIn(item["checkpoints"][0]["question"], second)
        request = json.loads(model.call_args.args[1])
        self.assertEqual(request["loi_da_giang"], ["Công cụ tạo ảnh cũng là LLM."])

    def test_reveals_after_two_hints_and_advances_when_learner_repairs(self):
        model = Mock(side_effect=[verdict("đúng", "sai")] * 3 + [verdict("đúng", "đúng")])
        self.assertTrue(self.session.explain("Công cụ ảnh là LLM.", model).startswith("AI người học"))
        self.assertTrue(self.session.explain("Tạo ảnh thì là LLM.", model).startswith("AI người học"))
        feedback = self.session.explain("Mình vẫn nghĩ ảnh do LLM làm.", model)
        self.assertIn("Giám khảo · [HIỂU SAI]", feedback)
        self.assertIn("[D01-P51]", feedback)
        self.assertIn(self.days[0]["source"], feedback)

        feedback = self.session.explain("GenAI tạo ảnh, LLM chuyên ngôn ngữ.", model)
        self.assertIn("Giám khảo · [ĐỦ Ý]", feedback)
        self.assertEqual(self.session.index, 1)
        self.assertEqual(self.session.hints, 0)
        self.assertEqual(self.session.history, [])

    def test_invalid_judge_reply_leaves_item_unchecked(self):
        model = Mock(return_value={"text": '{"relevant":true,"points":["đúng"]}'})
        with self.assertRaises(ValueError):
            self.session.explain("Một câu trả lời.", model)
        self.assertEqual(self.session.index, 0)
        self.assertEqual(self.session.hints, 0)
        self.assertEqual(self.session.statuses[0], "Chưa kiểm tra")


if __name__ == "__main__":
    unittest.main()
