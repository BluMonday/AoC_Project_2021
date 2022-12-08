import numpy as np
from scipy.optimize import curve_fit

if __name__ == '__main__':

    num_days = 256
    initial_fish_single = np.array([5], dtype=np.uint64)
    initial_fish_test = np.array([3,4,3,1,2], dtype=np.uint64)
    initial_fish = np.array([5,1,2,1,5,3,1,1,1,1,1,2,5,4,1,1,1,1,2,1,2,1,1,1,1,1,2,1,5,1,1,1,3,1,1,1,3,1,1,3,1,1,4,3,1,1,4,1,1,1,1,2,1,1,1,5,1,1,5,1,1,1,4,4,2,5,1,1,5,1,1,2,2,1,2,1,1,5,3,1,2,1,1,3,1,4,3,3,1,1,3,1,5,1,1,3,1,1,4,4,1,1,1,5,1,1,1,4,4,1,3,1,4,1,1,4,5,1,1,1,4,3,1,4,1,1,4,4,3,5,1,2,2,1,2,2,1,1,1,2,1,1,1,4,1,1,3,1,1,2,1,4,1,1,1,1,1,1,1,1,2,2,1,1,5,5,1,1,1,5,1,1,1,1,5,1,3,2,1,1,5,2,3,1,2,2,2,5,1,1,3,1,1,1,5,1,4,1,1,1,3,2,1,3,3,1,3,1,1,1,1,1,1,1,2,3,1,5,1,4,1,3,5,1,1,1,2,2,1,1,1,1,5,4,1,1,3,1,2,4,2,1,1,3,5,1,1,1,3,1,1,1,5,1,1,1,1,1,3,1,1,1,4,1,1,1,1,2,2,1,1,1,1,5,3,1,2,3,4,1,1,5,1,2,4,2,1,1,1,2,1,1,1,1,1,1,1,4,1,5], dtype=int)

    lanternfish = initial_fish

    lf = np.zeros(9,dtype=np.uint64)

    for i in range(1,6):
        lf[i] = np.sum(lanternfish == i)

    def grow_one_day(arr):
        arr[7] += arr[0] # fish at day 0 reset to day 6 + 1
        arr = np.append(arr[1:], arr[0]) # decrement all fish 1 and spawn new fish at counter 8
        return arr

    for i in range(num_days):
        lf = grow_one_day(lf)
        print(f'day {i+1} there are {np.sum(lf)} fish')

    lf_counts = [len(lanternfish)]
    print(f'Initial state: {lanternfish}')
    for i in range(num_days):
        lanternfish -= 1
        new_fish_count = 0
        for j in range(len(lanternfish)):
            if lanternfish[j] == -1:
                lanternfish[j] = 6
                new_fish_count += 1
        lanternfish = np.append(lanternfish, np.array(new_fish_count*[8], dtype=int))
        lf_counts.append(len(lanternfish))
        print(f'After {i+1} days {len(lanternfish)}: {lanternfish}')

    print(f'part 1: {len(lanternfish)} total fish')

    xdata = np.arange(0,len(lf_counts),dtype=int)
    ydata = np.array(lf_counts,dtype=int)

    import matplotlib.pyplot as plt
    plt.ion()

    plt.plot(xdata, ydata, 'k+')

    def func(x, a, b, c):
        return a * np.exp(b * x) + c


    popt, pcov = curve_fit(func, xdata, ydata)
    plt.plot(xdata, func(xdata, *popt), 'r-',
             label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

    initial_vals = np.arange(1,6)
    resulting_vals = np.zeros(6, dtype=int)
    for val in initial_vals:
        lanternfish = np.array([val], dtype=int)
        for i in range(num_days):
            lanternfish -= 1
            new_fish_count = 0
            for j in range(len(lanternfish)):
                if lanternfish[j] == -1:
                    lanternfish[j] = 6
                    new_fish_count += 1
            lanternfish = np.append(lanternfish, np.array(new_fish_count*[8], dtype=int))
        resulting_vals[val] = int(len(lanternfish))

    total_fish = 0
    for fish in initial_fish_test:
        total_fish += resulting_vals[fish]

    print(f'part 2: {total_fish} total fish')
    print('done')