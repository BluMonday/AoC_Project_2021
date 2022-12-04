class Assignment:
    start = []
    stop = []

    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def span(self) -> int:
        return self.stop - self.start

def check_overlap(a1: Assignment, a2: Assignment) -> bool:
    greater_span = []
    lesser_span = []
    if a1.span() >= a2.span():
        greater_span = a1
        lesser_span = a2
    else:
        greater_span = a2
        lesser_span = a1
    if (greater_span.start <= lesser_span.start) & (greater_span.stop >= lesser_span.stop):
        return True
    return False

def check_partial_overlap(a1: Assignment, a2: Assignment) -> bool:
    greater_start = []
    lesser_start = []
    if a1.start <= a2.start:
        lesser_start = a1
        greater_start = a2
    else:
        lesser_start = a2
        greater_start = a1
    return lesser_start.stop >= greater_start.start

def process_input(input):
    all_assignments = list()
    for line in input:
        line_assignments = list()
        split_line = line.split(',')
        for sl in split_line:
            start, stop = int(sl.split('-')[0]), int(sl.split('-')[1])
            line_assignments.append(Assignment(start, stop))
        all_assignments.append(line_assignments)
    return all_assignments


if __name__ == '__main__':
    f = open('input.txt')
    puzzle_input = f.read().split('\n')
    all_assignments = process_input(puzzle_input)

    total_overlaps = len([overlap for pair in all_assignments if (overlap := check_overlap(pair[0], pair[1]))])
    partial_overlaps = len([overlap for pair in all_assignments if (overlap := check_partial_overlap(pair[0], pair[1]))])

    print(f'Part 1: {total_overlaps}')
    print(f'Part 2: {partial_overlaps}')
    print('done')
