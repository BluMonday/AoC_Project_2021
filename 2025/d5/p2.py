from collections import defaultdict
from collections import namedtuple
from collections import deque


if __name__ == '__main__':

    f = open(f'in2.txt')
    inp_ranges, inp_ids = f.read().split('\n\n')
    inp_ranges = inp_ranges.split('\n')
    ranges = [[int(n) for n in x.split('-')] for x in inp_ranges]
    ids = inp_ids.split('\n')
    ids = [int(x) for x in ids]

    # sort ranges by first number
    ranges.sort()

    ans = 0
    start = ranges[0][0]
    end = ranges[0][1]
    ranges = ranges[1:]
    for r in ranges:
        if r[0] <= end:
            # next range overlaps
            pass
        else:
            # a gap in ranges, accumulate prev range
            ans += end-start +1
            # adjust set new current range
            start = r[0]
            end = r[1]
            continue
        if r[1] > end:
            # adjust current range end
            end = r[1]
            continue
    ans += end - start +1
    print(ans)
