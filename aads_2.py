import urllib.request
import time
import random
import sys
sys.setrecursionlimit(10**6)

# Code implementing fast sorting algorithms and comparing their execution time. Input is randomly generated for integers, while string inputs are taken from the URL.


# Loading the strings from the website and convert to list
url = 'http://norvig.com/ngrams/count_1w.txt'
response = urllib.request.urlopen(url)
words = response.read().decode().split('\n')
random_words = random.sample(words,50000)

# Generate random integers to sort
arrInt = [random.randint(1, 100) for i in range(100000)]

def check_if_sorted(arr):
    i = 1
    is_sorted = True
    while i < len(arr) and is_sorted:
        if arr[i - 1] > arr[i]:
            is_sorted = False
        i += 1
    return is_sorted

#Comparing elements that are far and gradually reduces the gap between them until they are adjacent
def shell_sort(arr):
    n = len(arr)
    gap = n // 2 #gap = h
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    assert check_if_sorted(arr), "Array is not sorted!"
    return arr

# selects a pivot element and partions other elements into two sub arrays, then sorts them
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        middle = []
        for i in arr[1:]:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                middle.append(i)
        arr = quick_sort(left) + middle + quick_sort(right)
    assert check_if_sorted(arr), "Array is not sorted!"
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#switchs to insertion sort for smaller arrays, otherwise with quicksort
def quick_sort_insertion(arr, threshold=10):
    if len(arr) <= threshold:
        insertion_sort(arr)
        assert check_if_sorted(arr), "Array is not sorted!"
        return arr
    else:
        quick_sort(arr)
        return arr

# Measure the execution time of each sorting function for int
start_time = time.time()
arr1=arrInt.copy()
shell_sort(arr1)
end_time = time.time()
print("Execution time for Shell Sort on integers:", end_time - start_time, "seconds")

start_time = time.time()
arr2=arrInt.copy()
quick_sort(arr2)
end_time = time.time()
print("Execution time for Quick Sort on integers:", end_time - start_time, "seconds")

start_time = time.time()
arr3=arrInt.copy()
quick_sort_insertion(arr3)
end_time = time.time()
print("Execution time for Quick Sort combined with Insertion Sort on integers:", end_time - start_time, "seconds")

# Measure the execution time of each sorting function for strings
start_time = time.time()
arr4=random_words.copy()
shell_sort(arr4)
end_time = time.time()
print("Execution time for Shell Sort on strings:", end_time - start_time, "seconds")

start_time = time.time()
arr5=random_words.copy()
quick_sort(arr5)
end_time = time.time()
print("Execution time for Quick Sort on strings:", end_time - start_time, "seconds")

start_time = time.time()
arr6=random_words.copy()
quick_sort_insertion(arr6)
end_time = time.time()
print("Execution time for Quick Sort combined with Insertion Sort on strings:", end_time - start_time, "seconds")
