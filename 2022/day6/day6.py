if __name__ == '__main__':
    f = open('input.txt')
    puzzle_input = f.read()
    seq = [x for x in puzzle_input]

    marker_len = 14
    idx = 0
    for i in range(len(seq)):
        s = set(seq[i:i+marker_len])
        if len(s) == marker_len:
            idx = i + marker_len
            break
    print(idx)
    print('done')
