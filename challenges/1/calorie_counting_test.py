import unittest

import calorie_counting


class TestMain(unittest.TestCase):

    def test_read_file_to_trimmed_array(self):
        filename = "test_input.txt"
        expected = [
            [1000, 2000, 3000],
            [4000],
            [5000, 6000],
            [7000, 8000, 9000],
            [10000]
        ]

        actual = calorie_counting.read_file_to_trimmed_array(filename)
        self.assertEqual(expected, actual)

    def test_find_most_calories(self):
        input = [
            [1000, 2000, 3000],
            [4000],
            [5000, 6000],
            [7000, 8000, 9000],
            [10000]
        ]
        expected = 4, 24000

        actual = calorie_counting.find_most_calories(input)

        self.assertEqual(expected, actual)

    def test_sort_descending(self):
        input = [
            [10000],
            [4000],
            [5000, 6000],
            [1000, 2000, 3000],
            [7000, 8000, 9000]
        ]

        expected = [
            [7000, 8000, 9000],
            [5000, 6000],
            [10000],
            [1000, 2000, 3000],
            [4000]
        ]

        self.assertEqual(expected, calorie_counting.sort_descending(input))

    def test_get_top_total(self):
        input = [
            [10000],
            [4000],
            [5000, 6000],
            [1000, 2000, 3000],
            [7000, 8000, 9000]
        ]

        expected = 45000

        self.assertEqual(expected, calorie_counting.get_top_total(input, 3))


if __name__ == '__main__':
    unittest.main()
