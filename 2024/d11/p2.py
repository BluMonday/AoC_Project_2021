from collections import defaultdict
from collections import namedtuple

def count_stones(stone_map):
    sum = 0
    for k, v in stone_map.items():
        sum += v
    return sum
def blink(key, value):
    if key == 0:
        # all stones return as value 1
        return [(1, value)]
    elif (dig := len(str(key))) % 2 == 0:
        s = str(key)
        k1 = int(s[:dig//2])
        k2 = int(s[dig//2:])
        # split to two stacks
        return [(k1, value), (k2, value)]
    else:
        # update value
        return [(key*2024, value)]

if __name__ == '__main__':

    blinks = 75
    f = open('in2.txt')
    inp = f.read().split(' ')
    stones = [int(x) for x in inp]
    stone_map = defaultdict(int)
    for s in stones:
        stone_map[s] += 1
    stone_map_prev = stone_map.copy()
    print(f'Initial: {len(stones)} stones')
    for i in range(blinks):
        stone_map.clear()
        for k, v in stone_map_prev.items():
            new_items = blink(k, v)
            for new_k, new_v in new_items:
                stone_map[new_k] += new_v
            pass
        print(f'Blink {i+1}: {count_stones(stone_map)} stones')
        stone_map_prev = stone_map.copy()

    pass
