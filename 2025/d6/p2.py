if __name__ == '__main__':

    config = 2
    f = open(f'in{config}.txt')
    inp = f.read().split('\n')
    operands = [x for x in inp[-1] if x != ' ']

    rows = inp[:config+2]
    problems = []
    problem = []
    for i in range(len(rows[0])):
        # read one columnized number as list of digits
        a = [rows[j][i] for j in range(len(rows))]
        a = [c.strip() for c in a]
        problem.append("".join(a))
        # detect new number
        if all([c == '' for c in a]):
            problems.append(problem[:-1])
            problem = []
        elif i == len(rows[0])-1:
            problems.append(problem)
            pass

    ans = 0
    for i in range(len(problems)):
        prob = [f"{x}{operands[i]}" for x in problems[i][:-1]]
        prob.append(problems[i][-1])
        prob = "".join(prob)
        ans += eval(prob)
        pass

    print(ans)
