from collections import defaultdict
from collections import namedtuple
from collections import deque


if __name__ == '__main__':

    config = 2
    f = open(f'in{config}.txt')
    inp_t, inp_d = f.read().split('\n\n')

    towels = [t.strip() for t in inp_t.split(',')]
    max_towel = max([len(t) for t in towels])
    designs = inp_d.split('\n')



    result = 0
    for design in designs:

        queue = deque()
        start = ''
        queue.append(start)
        success = False
        cache = set()

        while queue:
            current_t = queue.popleft()

            for t in towels:
                if (next_t := current_t + t) == design:
                    success = True
                    break
                elif len(next_t) > len(design): continue
                elif t == design[len(current_t):len(next_t)] and next_t not in cache:
                    queue.append(next_t)
                    cache.add(next_t)
        if success:
            result += 1


    print(result)
    pass
