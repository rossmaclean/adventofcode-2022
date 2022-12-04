import unittest

import rucksack_reorganisation


class TestMain(unittest.TestCase):

    def test_get_items_that_appear_in_both_compartments(self):
        cases = [
            ["ttgJtRGJQctTZtZT", ["t"]],
            ["PmmdzqPrVvPwwTWBwg", ["P"]]
        ]

        for case in cases:
            self.assertEqual(case[1],
                             rucksack_reorganisation.get_items_that_appear_in_both_compartments(
                                 case[0]))

    def test_get_priority_sum(self):
        cases = [
            ["p", 16],
            ["L", 38],
            ["P", 42],
            ["v", 22],
            ["t", 20],
            ["s", 19]
        ]

        for case in cases:
            self.assertEqual(case[1],
                             rucksack_reorganisation.get_priority_sum(case[0]))

    def test_get_sum_of_common_type_priorities(self):
        filename = 'test_input.txt'

        expected = 157

        self.assertEqual(expected,
                         rucksack_reorganisation.get_sum_of_common_type_priorities(
                             filename))

    def test_get_badge_priority_sum(self):
        filename = 'test_input.txt'
        expected = 70

        self.assertEqual(expected,
                         rucksack_reorganisation.get_badge_priority_sum(
                             filename))


if __name__ == '__main__':
    unittest.main()
