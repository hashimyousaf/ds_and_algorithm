import math

def binary_sarch(data_list, value):
    start = 0
    end = len(data_list) -1
    middle = math.floor((start+end)/2)

    while data_list[middle] != value and start <= end:
        if value < data_list[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)

    if data_list[middle] == value:
        return middle
    else:
        return -1

data_list = [3, 6, 8, 9, 16, 27, 34, 39, 40]

print(binary_sarch(data_list, 39))


