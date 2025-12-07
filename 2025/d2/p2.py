import numpy as np

if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split(',')
    answer = 0
    for x in inp:
        r1 = int(x.split('-')[0])
        r2 = int(x.split('-')[1])
        for n in range(r1, r2+1):
            n_s = str(n)
            # possible numbers of repetitions, i number of divisions
            for i in range(2, len(n_s)+1):
                # skip if not evenly divisible
                if len(n_s) % i != 0:
                    continue
                # l is length of chunks
                l = len(n_s)//i
                a = [n_s[j*l:(j+1)*l] for j in range(0, i)]
                if all(k == a[0] for k in a):
                    answer += n
                    # move to next ID
                    break
        pass

    print(answer)
    pass
