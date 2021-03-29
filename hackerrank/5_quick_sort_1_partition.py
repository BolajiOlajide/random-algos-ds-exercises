# https://www.hackerrank.com/challenges/quicksort1/problem?h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign
# runnig time = n * log(n)
def quickSort(arr):
    pivot = arr[0]

    left = []
    right = []

    for x in range(1, len(arr)):
        if arr[x] > pivot:
            right.append(arr[x])
        else:
            left.append(arr[x])

    return [*left, pivot, *right]

print(quickSort([4, 5, 3, 7, 2]))