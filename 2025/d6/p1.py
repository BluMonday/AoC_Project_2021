if __name__ == '__main__':

    config = 2
    f = open(f'in{config}.txt')
    inp = f.read().split('\n')
    operands = [x for x in inp[-1] if x != ' ']
    rows = [[x for x in n.split(' ') if x != ''] for n in inp[:config+2]]
    numbers = [list(row) for row in zip(*rows)]

    ans = 0
    for i in range(len(numbers)):
        prob = [f"{x}{operands[i]}" for x in numbers[i][:-1]]
        prob.append(numbers[i][-1])
        prob = "".join(prob)
        ans += eval(prob)
        pass

    print(ans)