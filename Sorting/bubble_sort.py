import math

def bubble_sort(arr):
    # Time complexity  = Nˆ2
    # Space complexity  = O(1)
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    print(arr)
def selection_sort(arr):
    # Time complexity  = Nˆ2
    # Space complexity  = O(1)
    for i in range(len(arr)):
        min_element_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_element_index]:
                min_element_index = j
        arr[min_element_index], arr[i] =  arr[i], arr[min_element_index]
    print(arr)

def insertion_sort(arr):
    # Time complexity  = Nˆ2
    # Space complexity  = O(1)
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j - 1] = arr[j-1], arr[j]
    return arr

def bucket_sort(customList):
    # Time complexity  = Nˆ2 if we use insertion sort to sort buckets, NlogN if we use quick sort.
    # Space complexity  = O(N)
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberofBuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList, l, r):
    # Time complexity  = NlogN if we use quick sort.
    # Space complexity  = O(N)
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList


def paritition(custom_list, low, high):
    i = low - 1
    pivot = custom_list[high]
    for j in range(low, high):
        if custom_list[j] <= pivot:
            i += 1
            custom_list[i], custom_list[j] = custom_list[j], custom_list[i]
    custom_list[i+1], custom_list[high] = custom_list[high], custom_list[i+1]

    return (i+1)

def quick_sort(custom_list, low, high):
    # Time complexity  = NlogN if we use quick sort.
    # Space complexity  = O(N)
    if low < high:
        pi = paritition(custom_list, low, high)
        quick_sort(custom_list, low, pi-1)
        quick_sort(custom_list, pi+1, high)

def heapify(custom_list, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and custom_list[l] < custom_list[smallest]:
        smallest = l
    if r < n and custom_list[r] < custom_list[smallest]:
        smallest = r

    if smallest != i:
        custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
        heapify(custom_list, n, smallest)

def heap_sort(custom_list):
    # Time complexity  = NlogN if we use quick sort.
    # Space complexity  = O(1)
    n = len(custom_list)
    for i in range(int(n/2)-1, -1, -1):
        heapify(custom_list, n, i)

    for i in range(n-1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heapify(custom_list, i, 0)
    custom_list.reverse()


arr_list = [5,9,3,1,2,8,4,7,6]
# arr_list = [5,9,3,1,2]

#bubble_sort(arr_list)
#selection_sort(arr_list)
#insertion_sort(arr_list)
#print(bucket_sort(arr_list))
# print(mergeSort(arr_list, 0, 8))
# quick_sort(arr_list, 0, 4)
heap_sort(arr_list)
print(arr_list)


