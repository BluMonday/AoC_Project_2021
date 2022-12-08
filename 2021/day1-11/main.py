# This is a sample Python script.
import numpy as np
import scipy as sp
import scipy.signal as sg
import matplotlib.pyplot as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open('day1.txt')
    lines = f.read().split('\n')
    readings = []
    for line in lines:
        readings.append(int(line))

    f.close()


    filt_readings = np.convolve(readings, [1, 1, 1], mode= 'valid')

    prev_reading = filt_readings[0]
    counter = 0
    for reading in filt_readings[1:]:
        if reading - prev_reading > 0:
            # print('(increased)')
            counter += 1
        prev_reading = reading

    fig2 = plt.subplot(1,2,1 )
    plt.xlabel('Reading #')
    plt.ylabel('Depth (m)')
    plt.plot(readings)
    fig2 = plt.subplot(1,2,2)
    plt.xlabel('Reading #')
    plt.ylabel('Depth (m)')
    plt.plot(filt_readings)
    plt.show()
    print('done')
