if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    answer = 0
    for x in inp:
        a = [int(n) for n in x]
        an = a
        j = []
        for d in range(12):
            l = 11-d
            if l == 0:
                dn = max(an)
            else:
                dn = max(an[:-l])
            idn = an.index(dn)
            an = an[idn+1:]
            j.append(str(dn))
        answer += int("".join(j))
        pass

    print(answer)
    pass
