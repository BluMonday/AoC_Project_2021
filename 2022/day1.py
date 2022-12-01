class Elf:
    calories = 0


if __name__ == '__main__':
    f = open('day1.txt')
    file_input = f.read().split('\n\n')

    elves = list()
    for snackbag in file_input:
        elf = Elf()
        snacks = snackbag.split('\n')
        elf.calories = sum([int(snack) for snack in snacks])
        elves.append(elf)

    calories = [elf.calories for elf in elves]
    calories.sort(reverse= True)
    max = calories[0]
    max3 = sum(calories[0:3])
    print(f'max: {max}')
    print(f'max of top three:{max3}')
    print('done')
