import unittest as ut
from dayone import puzzle_one, puzzle_two

f = open('day1_test.txt')
test_input = f.read()


class Test(ut.TestCase):
    def test_puzzle_one(self):
        self.assertEqual(puzzle_one(test_input), 24000)

    def test_puzzle_two(self):
        self.assertEqual(puzzle_two(test_input), 45000)


if __name__ == '__main__':
    ut.main()