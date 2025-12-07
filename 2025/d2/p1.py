if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split(',')
    answer = 0
    for x in inp:
        r1 = int(x.split('-')[0])
        r2 = int(x.split('-')[1])
        for n in range(r1, r2+1):
            n_s = str(n)
            a = str(n_s[:len(n_s)//2])
            b = str(n_s[len(n_s)//2:])
            if a == b:
                answer += n
        pass

    print(answer)
    pass
