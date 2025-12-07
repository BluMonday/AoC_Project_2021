if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    answer = 0
    for x in inp:
        a = [int(n) for n in x]
        d1 = max(a[:-1])
        id1 = a.index(d1)
        d2 = max(a[id1+1:])
        answer += int(str(d1)+str(d2))
        pass

    print(answer)
    pass
