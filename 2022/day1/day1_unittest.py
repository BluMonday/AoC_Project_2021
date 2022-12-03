from unittest import TestCase

from dayone import puzzle_one, puzzle_two

test_input = <input>

class Test(TestCase):
    def test_puzzle_one(self):
        self.assertEqual(puzzle_one(test_input), 24000)

    def test_puzzle_two(self):
        self.assertEqual(puzzle_two(test_input), 45000)