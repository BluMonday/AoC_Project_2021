def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96


if __name__ == '__main__':
    f = open('input.txt')
    puzzle_input = f.read().split('\n')

    priorities = list()
    for rucksack in puzzle_input:
        rucksack = [char for char in rucksack]
        compartment1 = set(rucksack[:len(rucksack)//2])
        compartment2 = set(rucksack[len(rucksack)//2:len(rucksack)])
        special_item = compartment1 & compartment2
        priorities.append(get_priority(special_item.pop()))

    print(sum(priorities))

    priorities2 = list()
    for index in range(0, len(puzzle_input), 3):
        rs1 = set([char for char in puzzle_input[index]])
        rs2 = set([char for char in puzzle_input[index+1]])
        rs3 = set([char for char in puzzle_input[index+2]])
        common_item = (rs1 & rs2 & rs3).pop()
        priorities2.append(get_priority(common_item))

    print(sum(priorities2))
    print('done')