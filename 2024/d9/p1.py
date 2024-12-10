from collections import defaultdict
from collections import namedtuple

def get_first_blank(disk):
    return disk.index('.')
def get_last_file(disk):
    for i in reversed(range(len(disk))):
        if disk[i] != '.':
            return i

def checksum(disk):
    i = 0
    sum = 0
    while True:
        if disk[i] == '.':
            break
        sum += disk[i] * i
        i += 1
    return sum

if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read()

    disk = []
    toggle = True
    file_idx = 0
    for c in inp:
        if toggle:
            disk += [file_idx for x in range(int(c))]
            file_idx += 1
        else:
            disk += ['.' for x in range(int(c))]
        toggle = not toggle

    while True:
        blank_idx = get_first_blank(disk)
        file_idx = get_last_file(disk)
        if blank_idx < file_idx:
            disk[blank_idx] = disk[file_idx]
            disk[file_idx] = '.'
        else:
            break
    print(checksum(disk))
    pass
