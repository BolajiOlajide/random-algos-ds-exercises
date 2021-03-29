def runningTime(arr):
    shift = 0
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]

        while (j >= 0) and (arr[j] > key):
            shift += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return shift

runningTime([2, 1, 3, 1, 2])