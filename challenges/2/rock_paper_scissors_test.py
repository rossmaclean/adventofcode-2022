import os.path
import unittest

import rock_paper_scissors


class TestMain(unittest.TestCase):

    def test_read_file_to_array(self):
        expected = [
            ["A", "Y"],
            ["B", "X"],
            ["C", "Z"]
        ]
        filename = "./test_input.txt"

        self.assertEqual(expected,
                         rock_paper_scissors.read_file_to_array(filename))

    def test_get_my_score_for_round(self):
        cases = [
            [["A", "Y"], 8],
            [["B", "X"], 1],
            [["C", "Z"], 6]
        ]

        for case in cases:
            self.assertEqual(case[1],
                             rock_paper_scissors.get_my_score_for_round(
                                 case[0]))

    def test_get_my_score_for_round_full_strat(self):
        cases = [
            [["A", "Y"], 4],
            [["B", "X"], 1],
            [["C", "Z"], 7]
        ]

        for case in cases:
            self.assertEqual(case[1],
                             rock_paper_scissors.get_my_score_for_round_full_strat(
                                 case[0]))

    def test_get_my_score_for_round_full_strat_real_input(self):
        input = rock_paper_scissors.read_file_to_array(
            os.path.realpath("./input.txt"))

        self.assertEqual(12526,
                         rock_paper_scissors.get_my_score_for_rounds_full_strat(
                             input))

    def test_get_my_score_for_rounds_full_strat(self):
        input = [
            ["A", "Y"],
            ["B", "X"],
            ["C", "Z"],
        ]

        self.assertEqual(12,
                         rock_paper_scissors.get_my_score_for_rounds_full_strat(
                             input))


if __name__ == '__main__':
    unittest.main()
