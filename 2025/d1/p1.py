if __name__ == '__main__':

    f = open('in2.txt')
    inp = f.read().split('\n')
    dialPos = 50
    answer = 0
    for x in inp:
        thisInp = int(x[1:])
        if x[0] == 'L':
            thisInp = -thisInp
        dialPos += thisInp
        dialPos = dialPos % 100
        if dialPos == 0:
            answer += 1

    print(answer)
    pass
