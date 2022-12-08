class point:
    center = []
    up = 9
    down = 9
    left = 9
    right = 9
    is_lowpoint = False
    x = []
    y = []

    def __init__(self, center, x, y):
        self.center = center
        self.x = x
        self.y = y

    def check_if_lowpoint(self):
        if self.center < min(self.down, self.left, self.right, self.up):
            self.is_lowpoint = True





if __name__ == '__main__':
    global basin

    def index_matrix(matrix, coord):
        return matrix[coord[0]][coord[1]]

    def get_basin_pts(matrix, coord):
        right = (coord[0], coord[1]+1)
        if index_matrix(matrix, right) is not 9 and right not in basin:
            basin.add(right)
            get_basin_pts(matrix, right)
        left = (coord[0], coord[1] - 1)
        if index_matrix(matrix, left) is not 9 and left not in basin:
            basin.add(left)
            get_basin_pts(matrix, left)
        up = (coord[0]-1, coord[1])
        if index_matrix(matrix, up) is not 9 and up not in basin:
            basin.add(up)
            get_basin_pts(matrix, up)
        down = (coord[0]+1, coord[1])
        if index_matrix(matrix, down) is not 9 and down not in basin:
            basin.add(down)
            get_basin_pts(matrix, down)
        return

    f = open('day9.txt')
    input = f.read().split('\n')

    matrix = [[9]+list(map(int, row))+[9] for row in input]
    width = len(matrix[0])
    nines = [9 for x in range(width)]
    matrix = [nines] + matrix + [nines]
    width = len(matrix[0])
    height = len([r[0] for r in matrix])

    lowpoints = []
    for x in range(1,width-1):
        for y in range(1,height-1):
            pt = point(matrix[y][x], x, y)
            if x > 0:
                pt.left = matrix[y][x-1]
            if x < width-1:
                pt.right = matrix[y][x+1]
            if y > 0:
                pt.up = matrix[y-1][x]
            if y < height-1:
                pt.down = matrix[y+1][x]
            pt.check_if_lowpoint()
            if pt.is_lowpoint:
                lowpoints.append(pt)

    sum = 0
    for pt in lowpoints:
        sum += pt.center + 1
    print(sum) # end part 1

    sizes = []
    for lowpt in lowpoints:
        basin = set()
        root_coord = (lowpt.y, lowpt.x)
        basin.add(root_coord)
        get_basin_pts(matrix, root_coord)
        sizes.append(len(basin))

    sizes.sort(reverse=True)

    print(sizes[0]*sizes[1]*sizes[2])

    print('done')

