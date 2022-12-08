import numpy as np

class sev_seg:

    def __init__(self, entry):
        self.sig_patterns = []
        self.sig_lengths = []
        self.outputs = []
        self.num_to_seg = {}
        self.seg_to_num = {}
        self.output_value = 0
        entry = entry.split('|')
        sp = entry[0].split(' ')[:-1]
        self.sig_patterns = np.array(sp, dtype=np.object_)
        self.sig_lengths = length(self.sig_patterns)
        op = entry[1].split(' ')[1:]
        self.outputs = np.array(op, dtype=np.object_)
        self.decode()


    def decode(self):
        # 1, 4, 7, and 8 are known by number of segments. Add them to code book
        self.seg_to_num[self.sig_patterns[self.sig_lengths == 2][0]] = 1
        self.seg_to_num[self.sig_patterns[self.sig_lengths == 4][0]] = 4
        self.seg_to_num[self.sig_patterns[self.sig_lengths == 3][0]] = 7
        self.seg_to_num[self.sig_patterns[self.sig_lengths == 7][0]] = 8

        self.num_to_seg[1] = self.sig_patterns[self.sig_lengths == 2][0]
        self.num_to_seg[4] = self.sig_patterns[self.sig_lengths == 4][0]
        self.num_to_seg[7] = self.sig_patterns[self.sig_lengths == 3][0]
        self.num_to_seg[8] = self.sig_patterns[self.sig_lengths == 7][0]

        # get 5 segment codes. These will be 2, 3, and 5
        five_seg = self.sig_patterns[self.sig_lengths == 5]

        # the index not included is digit 3. Remove 3 from unknown digits
        if    num_diffs(five_seg[0], five_seg[1]) == 2:
            self.seg_to_num[five_seg[2]] = 3
            self.num_to_seg[3] = five_seg[2]
            five_seg = np.delete(five_seg, 2)
        elif  num_diffs(five_seg[0], five_seg[2]) == 2:
            self.seg_to_num[five_seg[1]] = 3
            self.num_to_seg[3] = five_seg[1]
            five_seg = np.delete(five_seg, 1)
        elif  num_diffs(five_seg[1], five_seg[2]) == 2:
            self.seg_to_num[five_seg[0]] = 3
            self.num_to_seg[3] = five_seg[0]
            five_seg = np.delete(five_seg, 0)

        # decode 2 and 5
        for i in range(len(five_seg)):
            if num_diffs(self.num_to_seg[4], five_seg[i]) == 2:
                self.seg_to_num[five_seg[i]] = 5
                self.num_to_seg[5] = five_seg[i]
            else:
                self.seg_to_num[five_seg[i]] = 2
                self.num_to_seg[2] = five_seg[i]

        # get 6 segment codes. These will be 6, 9, and 0
        six_seg = self.sig_patterns[self.sig_lengths == 6]

        for i in range(len(six_seg)):
            if num_diffs(self.num_to_seg[1], six_seg[i]) == 5:
                self.seg_to_num[six_seg[i]] = 6
                self.num_to_seg[6] = six_seg[i]
            elif num_diffs(self.num_to_seg[4], six_seg[i]) == 2:
                self.seg_to_num[six_seg[i]] = 9
                self.num_to_seg[9] = six_seg[i]
            else:
                self.seg_to_num[six_seg[i]] = 0
                self.num_to_seg[0] = six_seg[i]

        self.output_str = ''
        for value in self.outputs:
            for seg in self.seg_to_num:
                if num_diffs(seg, value) == 0:
                    self.output_str += str(self.seg_to_num[seg])

        self.output_value = int(self.output_str)


def num_diffs( a, b):
    if len(a) > len(b): # make sure x is longer or equal length
        x = a
        y = b
    else:
        x = b
        y = a
    sum = 0
    for i in x: # count letters in x that are not in y
        if i not in y:
            sum += 1
    return sum

if __name__ == '__main__':
    f = open('day8.txt')
    entries = f.read().split('\n')

    length = np.vectorize(lambda x: len(x))
    displays = []
    signal_patterns = np.empty((len(entries), 10), dtype=np.object_)
    outputs = np.empty((len(entries), 4), dtype=np.object_)
    for i in range(len(entries)):
        split_entry = entries[i].split('|')
        sp_i = split_entry[0].split(' ')[:-1]
        o_i = split_entry[1].split(' ')[1:]
        signal_patterns[i, :] = np.array(sp_i, dtype=np.object_)
        outputs[i, :] = np.array(o_i, dtype=np.object_)
        displays.append(sev_seg(entries[i]))
        continue


    output_lengths = length(outputs)
    sum = 0
    for x in [2, 4, 3, 7]:
        sum += np.sum(output_lengths == x)

    print(f'part 1 total 1, 4, 7, 8 entries is: {sum}')

    sum = 0
    for display in displays:
        sum += display.output_value
    #sum -= displays[0].output_value
    print(f'part 2 sum of output values is: {sum}')

    print('done')