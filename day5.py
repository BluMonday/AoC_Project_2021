import numpy
import numpy as np
import matplotlib.pyplot as plt

class vent:
    x1, y1, x2, y2 = [], [], [], []
    diagonal = []

    def swap_coords(self):
        temp_x = self.x1
        temp_y = self.y1
        self.x1 = self.x2
        self.y1 = self.y2
        self.x2 = temp_x
        self.y2 = temp_y

    def __init__(self, vent_line):
        start_stop = vent_line.split(' -> ')
        start_stop = start_stop[0].split(',') + start_stop[1].split(',')
        start_stop = [int(coord) for coord in start_stop] # start stop is now x1...y2 as ints

        self.x1 = start_stop[0]
        self.y1 = start_stop[1]
        self.x2 = start_stop[2]
        self.y2 = start_stop[3]

        if start_stop[0] + start_stop[1] > start_stop[2] + start_stop[3]:
            self.swap_coords() # vent is always pointing away from origin

        if self.x1 == self.x2 or self.y1 == self.y2:
            self.diagonal = False
        else:
            self.diagonal = True


if __name__ == '__main__':
    plt.ion()
    f = open('day5.txt')
    file_input = f.read().split('\n')
    v1 = vent(file_input[0])
    vents = []

    for line in file_input:
        vents.append(vent(line))

    x = []
    y = []
    for vent in vents:
        x.append(vent.x2)
        y.append(vent.y2) # x2 and y2 are max coord
    max_x = max(x)
    max_y = max(y)

    vent_map = np.zeros((max_y+1, max_x+1), int) # vent map with size large enough to accomodate index of max_x/y

    for vent in vents:
        if vent.diagonal is False:
            vent_map[vent.y1:vent.y2+1, vent.x1:vent.x2+1] += 1

    overlaps = np.sum(vent_map > 1)

    plt.title('Part 1 plotted')
    plt.imshow(vent_map, cmap='hot')
    print(f'part 1, number of overlaps is: {overlaps}')

    for vent in vents:
        if vent.diagonal is True:
            step_x = int(vent.x2 - vent.x1 > 0)*2-1
            step_y = int(vent.y2 - vent.y1 > 0) * 2 - 1
            vent_map[(np.arange(vent.y1, vent.y2 + step_y, step_y), np.arange(vent.x1, vent.x2 + step_x, step_x))] += 1

    plt.title('Part 2 plotted')
    plt.imshow(vent_map, cmap='hot')
    overlaps = np.sum(vent_map > 1)
    print(f'part 2, number of overlaps is: {overlaps}')
    print('done')