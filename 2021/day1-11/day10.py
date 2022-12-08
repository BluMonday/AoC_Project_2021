if __name__ == '__main__':

    f = open('day10.txt')
    input = f.read().split('\n')

    o2c = {'(': ')', '[': ']', '<': '>', '{': '}'}
    c2o = {')': '(', ']': '[', '>': '<', '}': '{'}
    to_pts = {')': 3, ']': 57, '}': 1197, '>': 25137}
    to_pts2 = {')': 1, ']': 2, '}': 3, '>': 4}
    open = {'(', '<', '[', '{'}
    sum = 0
    incompletes = []
    for line in input:
        valid = True
        buffer = list()
        chars = [x for x in line]
        for char in chars:
            if char in open:
                buffer.append(char)
            elif o2c[buffer[-1]] == char:
                buffer.pop()
            # if char is of the wrong type
            else:
                sum += to_pts[char]
                a = o2c[buffer[-1]]
                b = char
                #print(f"Expected {a}, but found {b} instead.")
                valid = False
                break
        if valid:
            incompletes.append(buffer)

    print(f'score is {sum}')

    scores = list()
    for seq in incompletes:
        seq.reverse()
        seq = [o2c[x] for x in seq]
        score = 0
        for char in seq:
            score *= 5
            score += to_pts2[char]
        scores.append(score)

    scores.sort()

    print(f'part 2 score is {scores[len(scores)//2]}')
    print('done')