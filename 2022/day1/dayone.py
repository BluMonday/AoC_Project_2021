from typing import List


def puzzle_one(puzzle_input: str) -> int:
    return max([sum(entry) for entry in _process_puzzle_input(puzzle_input)])


def puzzle_two(puzzle_input: str) -> int:
    sums = sorted([sum(entry) for entry in _process_puzzle_input(puzzle_input)], reverse=True)
    return sum(sums[0:3])


def _process_puzzle_input(puzzle_input: str) -> List[List[int]]:
    return [[int(entry) for entry in calories.split('\n')] for calories in puzzle_input.split('\n\n')]