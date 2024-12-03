if __name__ == '__main__':
    f = open('input.txt')
    rows = f.read().split('\n')
    left_list = []
    right_list = []
    for i in range(len(rows)):
        row = rows[i].split('   ')
        left_list.append(int(row[0]))
        right_list.append(int(row[1]))
    left_list.sort()
    right_list.sort()
    sum = 0
    for i in range(len(left_list)):
        sum += abs(left_list[i]-right_list[i])
    print(sum)