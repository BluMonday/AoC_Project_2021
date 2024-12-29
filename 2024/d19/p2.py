from collections import defaultdict
from collections import namedtuple
from collections import deque


if __name__ == '__main__':

    config = 1
    f = open(f'in{config}.txt')
    inp_t, inp_d = f.read().split('\n\n')

    towels = [t.strip() for t in inp_t.split(',')]
    max_towel = max([len(t) for t in towels])
    designs = inp_d.split('\n')
    #designs = [designs[1]]

    results = []
    for design in designs:

        queue = deque()
        start = ''
        queue.append(start)
        cache = defaultdict(lambda: 0)
        result = 0

        while queue:
            current_t = queue.popleft()

            for t in towels:
                if (next_t := current_t + t) == design:
                    cache[next_t] += cache[current_t]
                elif len(next_t) > len(design): continue
                elif t != design[len(current_t):len(next_t)]: continue
                elif cache[next_t] == 0:
                    cache[next_t] += 1
                    queue.append(next_t)
                else:
                    cache[next_t] += 1
        results.append(cache[design])



    print(sum(results))
    pass
