from collections import defaultdict
from collections import namedtuple


class Stone:
    def __init__(self, v):
        self.v = v
    def blink(self):
        global stones
        if self.v == 0:
            self.v = 1
        elif (dig := len(str(self.v))) % 2 == 0:
            s = str(self.v)
            s1 = int(s[:dig//2])
            s2 = int(s[dig//2:])
            self.v = s1
            stones.append(Stone(s2))
        else:
            self.v = self.v * 2024
        return



if __name__ == '__main__':

    f = open('in1.txt')
    inp = f.read().split(' ')
    stones = [Stone(int(x)) for x in inp]
    stones_prev = stones.copy()
    blinks = 25
    print(f'Initial: {len(stones)} stones')
    for i in range(blinks):
        for s in stones_prev:
            s.blink()
            pass
        print(f'Blink {i+1}: {len(stones)} stones')
        stones_prev = stones.copy()

    pass
