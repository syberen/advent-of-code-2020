import unittest

from solution import get_seat_id


class TestFunctions(unittest.TestCase):
    def test_get_seat_id(self):
        """ Assert that get_seat_info returns the right data for given input """

        self.assertEqual(get_seat_id('BFFFBBFRRR'), 567)
        self.assertEqual(get_seat_id('FFFBBBFRRR'), 119)
        self.assertEqual(get_seat_id('BBFFBBFRLL'), 820)


if __name__ == '__main__':
    unittest.main()
