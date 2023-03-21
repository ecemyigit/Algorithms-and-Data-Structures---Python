import random
import time

# Code implementing basic sorting algorithms and comparing their execution time. Input is randomly generated for both integer and strings

def check_if_sorted(arr):
    i = 1
    is_sorted = True
    while i < len(arr) and is_sorted:
        if arr[i - 1] > arr[i]:
            is_sorted = False
        i += 1
    return is_sorted

#Repeatedly finding the minimum element in the unsorted array
def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
       
#Iterates through each element, compares current with sorted subarray and inserts it to its place
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr


##Compare each adjacent pair and check if they are in order. If not, swap them.
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Improved: By using a temporary variable (key), we make swapping faster
def insertionSort2(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def sortTest(arr):
    start_time = time.time()
    arr1 = arr.copy()
    selectionSort(arr1)
    selectionSortTime = time.time() - start_time
    is_sorted = check_if_sorted(arr1)

    start_time = time.time()
    arr2 = arr.copy()
    insertionSort(arr2)
    insertionSortTime = time.time() - start_time
    is_sorted = check_if_sorted(arr2)

    start_time = time.time()
    arr3 = arr.copy()
    bubbleSort(arr3)
    bubbleSortTime = time.time() - start_time
    is_sorted = check_if_sorted(arr3)

    start_time = time.time()
    arr4 = arr.copy()
    insertionSort2(arr4)
    insertionSort2Time = time.time() - start_time
    is_sorted = check_if_sorted(arr4)

    return (selectionSortTime, insertionSortTime, bubbleSortTime, insertionSort2Time, is_sorted)

def test():
    arrInt = [random.randint(1, 100) for i in range(300)] #Randomly generating integers 
    arrStr = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 10))) for i in range(200)] #Randomly generating strings

    selectionSortTimeInt, insertionSortTimeInt, bubbleSortTimeInt, insertionSort2TimeInt, is_sorted_int = sortTest(arrInt)
    selectionSortTimeStr, insertionSortTimeStr, bubbleSortTimeStr, insertionSort2TimeStr, is_sorted_str = sortTest(arrStr)

    print("Execution times for integer array:")
    print("Selection sort time: %.6f seconds" % selectionSortTimeInt)
    print("Insertion sort time: %.6f seconds" % insertionSortTimeInt)
    print("Bubble sort time: %.6f seconds" % bubbleSortTimeInt)
    print("Insertion sort 2 time: %.6f seconds" % insertionSort2TimeInt)
    print("Array sorted: ", is_sorted_int)
    print("")

    print("Execution times for string array:")
    print("Selection sort time: %.6f seconds" % selectionSortTimeStr)
    print("Insertion sort time: %.6f seconds" % insertionSortTimeStr)
    print("Bubble sort time: %.6f seconds" % bubbleSortTimeStr)
    print("Insertion sort 2 time: %.6f seconds" % insertionSort2TimeStr)

    print("Array sorted: ", is_sorted_str)


if __name__ == "__main__":
    test()
