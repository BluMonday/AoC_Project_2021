from collections import defaultdict
from collections import namedtuple

class Rule():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def check(self, update):
        if self.first in update and self.second in update:
            first_idx = update.index(self.first)
            second_idx = update.index(self.second)
            if  first_idx > second_idx:
                return False
        return True

if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n\n')
    inp_rules = inp[0].split('\n')
    rules = []
    for r in inp_rules:
        a,b = r.split('|')
        rules.append(Rule(int(a), int(b)))

    inp_updates = inp[1].split('\n')
    updates = []
    for line in inp_updates:
        updates.append([int(x) for x in line.split(',')])

    result = 0
    for update in updates:
        r = [rule.check(update) for rule in rules]
        if False not in r: result += update[len(update)//2]


    print(result)