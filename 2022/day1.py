class Elf:
    calories = 0

if __name__ == '__main__':
    f = open('day1.txt')
    file_input = f.read().split('\n')

    elfs = list()
    elf = Elf()
    for line in file_input:
        if line == '':
            elfs.append(elf)
            elf = Elf()
            continue
        else:
            elf.calories += int(line)
            continue
    elfs.append(elf)

    calories = [e.calories for e in elfs]
    max = max(calories)
    calories.sort(reverse= True)
    max3 = calories[0] + calories[1] + calories[2]
    print(f'max: {max}')
    print(f'max of top three:{max3}')
    print('done')