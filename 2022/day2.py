if __name__ == '__main__':
    f = open('day2.txt')
    puzzle_input = f.read().split('\n')

    decipher_input = dict()
    decipher_input['A'] = 'R'
    decipher_input['B'] = 'P'
    decipher_input['C'] = 'S'
    decipher_input['X'] = 'R'
    decipher_input['Y'] = 'P'
    decipher_input['Z'] = 'S'

    score_shape = dict()
    score_shape['R'] = 1
    score_shape['P'] = 2
    score_shape['S'] = 3

    score_result = dict()
    score_result['L'] = 0
    score_result['D'] = 3
    score_result['W'] = 6

    judge_round = dict()
    judge_round[('R','R')] = 'D'
    judge_round[('R','P')] = 'W'
    judge_round[('R','S')] = 'L'
    judge_round[('P', 'R')] = 'L'
    judge_round[('P', 'P')] = 'D'
    judge_round[('P', 'S')] = 'W'
    judge_round[('S', 'R')] = 'W'
    judge_round[('S', 'P')] = 'L'
    judge_round[('S', 'S')] = 'D'

    apply_strat = dict()
    apply_strat[('R', 'X')] = 'S'
    apply_strat[('R', 'Y')] = 'R'
    apply_strat[('R', 'Z')] = 'P'
    apply_strat[('P', 'X')] = 'R'
    apply_strat[('P', 'Y')] = 'P'
    apply_strat[('P', 'Z')] = 'S'
    apply_strat[('S', 'X')] = 'P'
    apply_strat[('S', 'Y')] = 'S'
    apply_strat[('S', 'Z')] = 'R'

    rounds = [round.split(' ') for round in puzzle_input]
    rounds1 = [(decipher_input[round[0]], decipher_input[round[1]]) for round in rounds]
    rounds2 = [(decipher_input[round[0]], round[1]) for round in rounds]
    rounds2 = [(round[0], apply_strat[tuple(round)]) for round in rounds2]
    scores1 = [score_shape[round[1]] + score_result[judge_round[round]] for round in rounds1]
    scores2 = [score_shape[round[1]] + score_result[judge_round[round]] for round in rounds2]

    print(f'part 1: {sum(scores1)}')
    print(f'part 2: {sum(scores2)}')

    print('done')
