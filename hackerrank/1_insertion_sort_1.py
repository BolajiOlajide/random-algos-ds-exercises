# https://www.hackerrank.com/challenges/insertionsort1/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign&isFullScreen=true&h_r=next-challenge&h_v=zen

def insertionSort1(n, arr):
    unsorted_value = arr[n - 1]

    for x in range(n, 0, -1):
        index_to_check = x - 2

        lower_match_found = arr[index_to_check] < unsorted_value
        value_to_replace = unsorted_value if (lower_match_found or index_to_check < 0) else arr[index_to_check]
        arr[x - 1] = value_to_replace
        print(' '.join(map(str, arr)))

        if lower_match_found:
            break

# insertionSort1(5, [1, 2, 4, 5, 3])
# insertionSort1(5, [2, 4, 6, 8, 3])
insertionSort1(5, [2, 4, 6, 8, 1])
