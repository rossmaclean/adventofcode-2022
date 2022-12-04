import unittest

import camp_cleanup


class TestMain(unittest.TestCase):

    def test_read_file_to_array(self):
        filename = "test_input.txt"

        expected = [
            [[2, 4], [6, 8]],
            [[2, 3], [4, 5]],
            [[5, 7], [7, 9]],
            [[2, 8], [3, 7]],
            [[6, 6], [4, 6]],
            [[2, 6], [4, 8]]
        ]

        self.assertEqual(expected, camp_cleanup.read_file_to_array(filename))

    def test_get_num_pairs_which_fully_contain_other_test_input(self):
        filename = "test_input.txt"
        pairs = camp_cleanup.read_file_to_array(filename)

        expected = 2

        self.assertEqual(expected,
                         camp_cleanup.get_num_pairs_which_fully_contain_other(
                             pairs))

    def test_get_num_pairs_which_fully_contain_other_real_input(self):
        filename = "input.txt"
        pairs = camp_cleanup.read_file_to_array(filename)

        expected = 305

        self.assertEqual(expected,
                         camp_cleanup.get_num_pairs_which_fully_contain_other(
                             pairs))

    def test_get_num_pairs_which_partially_contain_other_test_input(self):
        filename = "test_input.txt"
        pairs = camp_cleanup.read_file_to_array(filename)

        expected = 4

        self.assertEqual(expected,
                         camp_cleanup.test_get_num_pairs_which_partially_contain_other(
                             pairs))

    def test_get_num_pairs_which_partially_contain_other_real_input(self):
        filename = "input.txt"
        pairs = camp_cleanup.read_file_to_array(filename)

        expected = 811

        self.assertEqual(expected,
                         camp_cleanup.test_get_num_pairs_which_partially_contain_other(
                             pairs))


if __name__ == '__main__':
    unittest.main()
