import random

#функция нахождения раздела
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)
    return arr


def randomize_array():
    arr = []
    lenght = random.randint(0, 100)
    for i in range(lenght):
        arr.append(random.randint(0, 1000))
    return arr


array = randomize_array()
print(array)
lenght = len(array)
if lenght != 0:
    print(quickSort(array, 0, lenght-1))
else:
    print(quickSort(array, 0, lenght))

print("ZZZZZZZ GOOOOOOL GOIDA")

#tests
assert(quickSort([], 0, 0) == [])
assert(quickSort([1], 0, 0) == [1])
assert(quickSort([4, 5, 3, 1, 2], 0, 4) == [1, 2, 3, 4, 5])
assert(quickSort([2, 4, 3, 1], 0, 3) == [1, 2, 3, 4])