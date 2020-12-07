import unittest
from functions import find_pair, find_triplet


class TestFunctions(unittest.TestCase):
    def test_find_pair(self):
        """ Assert that find_pair returns a set with the right values for given input """
        input = [753, 18, 198, 598, 1267, 863]

        self.assertEqual(find_pair(input, 2020), {753, 1267})

    def test_find_triplet(self):
        """ Assert that find_triplet returns a set with the right values for given input """
        input = [705, 18, 533, 598, 782, 863]

        self.assertEqual(find_triplet(input, 2020), {705, 533, 782})


if __name__ == '__main__':
    unittest.main()
