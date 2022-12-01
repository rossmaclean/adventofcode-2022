import unittest

import main


class TestMain(unittest.TestCase):

    def test_add(self):
        expected = 15

        self.assertEqual(expected, main.add(10, 5))


if __name__ == '__main__':
    unittest.main()
