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
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        sum += disk[i] * i
    return sum

if __name__ == '__main__':

    f = open('in1.txt')
    inp = f.read()
    fileID_to_size = {}
    disk = []
    toggle = True
    file_idx = 0
    for c in inp:
        if toggle:
            disk += [file_idx for x in range(int(c))]
            # file ID to file length
            fileID_to_size[file_idx] = int(c)
            file_idx += 1
        else:
            disk += ['.' for x in range(int(c))]
        toggle = not toggle



    for i in reversed(range(file_idx)):
        pass
    pass
    print(checksum(disk))
