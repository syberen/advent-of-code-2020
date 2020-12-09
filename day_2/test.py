import unittest
from functions import get_count_with_limits, get_count_with_positions

test_data = [
    {
        'low_number': 11,
        'high_number': 17,
        'match_letter': 'z',
        'code': 'hwzdfvbpbxzfpjwmzq'
    },
    {
        'low_number': 1,
        'high_number': 11,
        'match_letter': 'm',
        'code': 'mxkmnxfbtnmvmtzdqjl'
    },
    {
        'low_number': 3,
        'high_number': 4,
        'match_letter': 'd',
        'code': 'dddajg'
    },
    {
        'low_number': 17,
        'high_number': 18,
        'match_letter': 'b',
        'code': 'jnlntbblbbqbkqmbbb'
    },
]


class TestFunctions(unittest.TestCase):
    def test_find_pair(self):
        """ Assert that get_count_with_limits returns the right number for given input """

        self.assertEqual(get_count_with_limits(test_data), 2)

    def test_find_triplet(self):
        """ Assert that get_count_with_limits returns the right number for given input """

        self.assertEqual(get_count_with_positions(test_data), 1)


if __name__ == '__main__':
    unittest.main()
