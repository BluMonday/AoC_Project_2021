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
        answer += abs(dialPos // 100)
        dialPos = dialPos % 100

    print(answer)
    pass
