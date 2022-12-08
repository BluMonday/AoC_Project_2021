import numpy as np

class bingo_board:
    matrix = []
    called_squares = []
    win = False

    def __init__(self, matrix):
        self.matrix = matrix
        self.called_squares = matrix < 0 # start at all false

    def call_number(self, number):
        self.called_squares = np.logical_or(self.called_squares, self.matrix == number)
        self.check_for_win()

    def check_for_win(self):
        for i in range(self.matrix.shape[0]):
            if np.all(self.called_squares[i, :]) | np.all(self.called_squares[:, i]): #check i'th row and col for all true
                self.win = True
                return True

    def sum_of_uncalled(self):
        return np.sum(self.matrix[np.logical_not(self.called_squares)])

if __name__ == '__main__':
    f = open('day4.txt')
    file_input = f.read().split('\n')

    bingo_numbers = file_input[0].split(',')
    bingo_numbers = [int(num_str) for num_str in bingo_numbers]

    boards = []
    for i in range((int((len(file_input)-1)/6))):
        bingo_list = []
        for row in file_input[i*6+2: i*6+2+5]:
            row = row.split(' ')
            while '' in row: row.remove('')
            row = [int(num_str) for num_str in row]
            bingo_list.append(row)
        boards.append(bingo_board(np.array(bingo_list)))

    win_board_index = []
    win_number = []
    for bingo_number in bingo_numbers:
        for i in range(len(boards)):
            boards[i].call_number(bingo_number)
            if boards[i].win:
                win_board_index = i
                win_number = bingo_number
                break
        else:
            continue
        break

    uncalled_sum = boards[win_board_index].sum_of_uncalled()
    print(f'sum of uncalled squares: {uncalled_sum}')
    print(f'winning number: {win_number}')
    print(f'solution part 1: {win_number*uncalled_sum}')

    lose_sum = []
    lose_number = []
    for bingo_number in bingo_numbers:
        for i in range(len(boards)):
            boards[i].call_number(bingo_number)
        if len(boards) > 1:
            boards = [board for board in boards if board.win is False] # prune won boards
        elif boards[i].win is False:
            continue
        else:
            lose_number = bingo_number
            lose_sum = boards[i].sum_of_uncalled()
            break

    print('--------------part 2 ---------------')
    print(f'sum of uncalled squares: {lose_sum}')
    print(f'winning number: {lose_number}')
    print(f'solution part 2: {lose_number*lose_sum}')


    print('done')

