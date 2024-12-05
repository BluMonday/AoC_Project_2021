def check_report(report):
    first_diff = []
    for i in range(len(report) - 1):
        first_diff.append(report[i + 1] - report[i])

    if first_diff[0] < 0:
        y = [x for x in first_diff if x <= -4 or x >= 0]
        if len(y) == 0:
            return True
    elif first_diff[0] > 0:
        y = [x for x in first_diff if x <= 0 or x >= 4]
        if len(y) == 0:
            return True
    else:
        return False

if __name__ == '__main__':
    f = open('input.txt')
    rows = f.read().split('\n')
    safe = 0
    for row in rows:
        report = [int(x) for x in row.split(' ')]
        if check_report(report) is True:
            safe += 1
        else:
            for i in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(i)
                if check_report(report_copy):
                    safe += 1
                    break



    print(safe)