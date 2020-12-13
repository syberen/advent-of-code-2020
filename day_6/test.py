import unittest

from solution import count_unique_group_answers, count_unanimous_group_answers


class TestFunctions(unittest.TestCase):
    def setUp(self):
        with open('test_input.txt', 'r') as input:
            self.input = input.read()

    def test_count_unique_group_answers(self):
        """ Assert that count_unique_group_answers returns the right number for given input """

        self.assertEqual(count_unique_group_answers(self.input), 11)

    def test_count_unanimous_group_answers(self):
        """ Assert that count_unanimous_group_answers returns the right number for given input """

        self.assertEqual(count_unanimous_group_answers(self.input), 6)


if __name__ == '__main__':
    unittest.main()
