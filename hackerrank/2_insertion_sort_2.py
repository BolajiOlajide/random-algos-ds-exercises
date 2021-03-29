# https://www.hackerrank.com/challenges/insertionsort2/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign&isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def insertionSort2(n, arr):
    for x in range(1, n):
        new_index = None
        current_iteration_value = arr[x]

        for y in range(x - 1, -1, -1):
            if current_iteration_value < arr[y]:
                new_index = y

        if new_index != None:
            arr.pop(x)
            arr.insert(new_index, current_iteration_value)
        print(' '.join(map(str, arr)))

# insertionSort2(6, [1, 4, 3, 5, 6, 2])
insertionSort2(8, [8,7,6,5,4,3,2,1])