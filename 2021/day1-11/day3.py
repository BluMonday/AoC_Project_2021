import numpy as np

if __name__ == '__main__':
    f = open('day3.txt')
    numbers = f.read().split('\n')


    bit_arr = []
    array_of_arrays = []
    for number in numbers:
        bits = [char for char in number]
        temp = []
        for bit in bits:
            temp.append(int(bit))
        array_of_arrays.append(temp)
    matrix = np.array(array_of_arrays)
    orig_matrix = matrix
    matrix = matrix * 2 -1
    sums = []
    for i in range(0,matrix.shape[1]):
        sum = 0
        for tick in matrix[:,i]:
            sum += tick
        sums.append(sum)

    sums.reverse()

    gamma = 0
    epsilon = 0
    for i in range(matrix.shape[1]):
        if sums[i] > 0:
            gamma += 1 << i
        else:
            epsilon += 1 << i
    print( gamma * epsilon)

    oxy_mat = matrix
    co2_mat = matrix


    for i in range(orig_matrix.shape[1]): # for each column, descending
        if oxy_mat.shape[0] == 1:
            break
        sum = oxy_mat[:, i].sum()
        if sum >= 0:
            oxy_mat = oxy_mat[oxy_mat[:, i] > 0, :]
        else:
            oxy_mat = oxy_mat[oxy_mat[:, i] < 0, :]

    for i in range(orig_matrix.shape[1]):
        if co2_mat.shape[0] == 1:
            break
        sum = -co2_mat[:, i].sum() # sum has the same sign as the less common
        if sum > 0: # keep ones if one is less common
            co2_mat = co2_mat[co2_mat[:, i] > 0, :]
        else: # else keep zeros
            co2_mat = co2_mat[co2_mat[:, i] < 0, :]
        print(i)
    
    
    oxy = 0
    co2 = 0
    for i in range(oxy_mat.shape[1]):
        if oxy_mat[0, -(i+1)] > 0:
            oxy += 1 << i
        if co2_mat[0, -(i + 1)] > 0:
            co2 += 1 << i

    print(f'oxygen rating is: {oxy}')
    print(f'co2 rating is :{co2}')
    print(f'life support rating is: {oxy*co2}')
    print('done')