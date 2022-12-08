def scenic_score(trees, x, y):
    center = trees[y][x]
    n = [t[x] for t in trees[:y]]
    n.reverse()
    s = [t[x] for t in trees[y + 1:]]
    w = trees[y][:x]
    w.reverse()
    e = trees[y][x + 1:]

    score = 1
    for dir in [n, s, e, w]:
        local_score = 0
        for t in dir:
            local_score += 1
            if t < center:
                continue
            else:
                break
        score *= local_score
    return score

def check_dir(center, compare):
    if len(compare) == 0:
        return True
    compare.sort(reverse= True)
    return center > compare[0]

def check_tree(trees, x, y):
    center = trees[y][x]
    n = [t[x] for t in trees[:y]]
    s = [t[x] for t in trees[y+1:]]
    w = trees[y][:x]
    e = trees[y][x+1:]

    visible_trees = 0
    for direction in [n, s, w, e]:
        if check_dir(center, direction):
            visible_trees += 1
            break

    return visible_trees

if __name__ == '__main__':
    f = open('input.txt')
    puzzle_input = f.read()
    as_rows = puzzle_input.split('\n')

    trees = [[int(x) for x in row] for row in as_rows]

    xs = len(trees[0])
    ys = len([t[0] for t in trees[:]])

    scenic_score(trees, 3, 0)
    scenic_scores = list()
    visible_trees = 0
    for x in range(xs):
        for y in range(ys):
            visible_trees += check_tree(trees, x, y)
            scenic_scores.append(scenic_score(trees, x, y))

    print(visible_trees)
    scenic_scores.sort()
    print(scenic_scores[-1])
    print('done')