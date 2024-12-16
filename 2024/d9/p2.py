from collections import defaultdict
from collections import namedtuple
class File(namedtuple('File', 'start stop')):
    def __str__(self):
        return f'{self.start},{self.stop},len={self.stop - self.start + 1}'
    def length(self):
        return self.stop - self.start + 1
def write_file(disk, file, id):
    for i in range(file.start, file.stop +1):
        disk[i] = id
def erase_file(disk, file):
    for i in range(file.start, file.stop +1):
        disk[i] = '.'
def move_file(disk, file_from, file_to, id):
    write_file(disk, file_to, id)
    erase_file(disk, file_from)

def find_file(disk, file_id):
    indices = [i for i, x in enumerate(disk) if x == file_id]
    return File(indices[0], indices[-1])

def find_all_blanks(disk):
    blanks = []
    in_blank = False
    start_idx = 0
    for i in range(len(disk)):
        if disk[i] == '.' and not in_blank:
            in_blank = True
            start_idx = i
        elif disk[i] == '.' and in_blank:
            continue
        elif disk[i] != '.' and in_blank:
            in_blank = False
            end_idx = i-1
            blanks.append(File(start_idx, end_idx))
        elif disk[i] != '.' and not in_blank:
            continue
    return blanks

def get_first_blank(disk):
    return disk.index('.')
def get_last_file(disk):
    for i in reversed(range(len(disk))):
        if disk[i] != '.':
            return i

if __name__ == '__main__':

    f = open('in2.txt')
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
    file_idx -= 1

    for f_id in range(file_idx,0,-1):
        blanks = find_all_blanks(disk)
        file = find_file(disk, f_id)
        for b in blanks:
            if b.length() >= file.length() and b.start < file.start:
                file_to = File(b.start, b.start + file.length() - 1)
                move_file(disk, file, file_to, f_id)
                break

print(sum([i*x for i, x in enumerate(disk) if x != '.']))
