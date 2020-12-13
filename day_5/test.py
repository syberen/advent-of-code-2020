import unittest

from solution import get_seat_info


class TestCount(unittest.TestCase):
    def test_count_valid_passports_by_fields_present(self):
        """ Assert that get_seat_info returns the right data for given input """

        self.assertEqual(get_seat_info('BFFFBBFRRR'), (70, 7, 567))
        self.assertEqual(get_seat_info('FFFBBBFRRR'), (14, 7, 119))
        self.assertEqual(get_seat_info('BBFFBBFRLL'), (102, 4, 820))


if __name__ == '__main__':
    unittest.main()
