import unittest
from solution import count_encountered_trees

test_data = ['..##.......',
             '#...#...#..',
             '.#....#..#.',
             '..#.#...#.#',
             '.#...##..#.',
             '..#.##.....',
             '.#.#.#....#',
             '.#........#',
             '#.##...#...',
             '#...##....#',
             '.#..#...#.#']


class TestCount(unittest.TestCase):
    def test_three_right_one_down(self):
        """ Assert that count_encountered_trees returns the right number for given input """

        self.assertEqual(count_encountered_trees(test_data, 3, 1), 7)

    def test_two_right_two_down(self):
        """ Assert that count_encountered_trees returns the right number for given input """

        self.assertEqual(count_encountered_trees(test_data, 2, 2), 1)


if __name__ == '__main__':
    unittest.main()
