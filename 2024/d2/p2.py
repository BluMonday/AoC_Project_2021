if __name__ == '__main__':
    f = open('input.txt')
    rows = f.read().split('\n')
    safe = 0
    for row in rows:
        report = [int(x) for x in row.split(' ')]
        first_diff = []
        for i in range(len(report)-1):
            first_diff.append(report[i+1] - report[i])
        y = [x for x in first_diff if x <= -4 or x >= 0]
        if len(y) <= 1:
            safe += 1
            continue
        y = [x for x in first_diff if x <= 0 or x >= 4]
        if len(y) <= 1:
            safe += 1


    print(safe)