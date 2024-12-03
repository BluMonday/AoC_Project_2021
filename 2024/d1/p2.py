if __name__ == '__main__':
    f = open('input.txt')
    rows = f.read().split('\n')
    left_list = []
    right_list = []
    for i in range(len(rows)):
        row = rows[i].split('   ')
        left_list.append(int(row[0]))
        right_list.append(int(row[1]))
    id_dict = {}
    for x in left_list:
        id_dict[x] = 0
    for x in right_list:
        if x in id_dict:
            id_dict[x] += 1
    score = 0
    for x in left_list:
        score += x * id_dict[x]

    print(score)