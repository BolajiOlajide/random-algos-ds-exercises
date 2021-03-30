# https://www.hackerrank.com/challenges/countingsort2/problem?h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&isFullScreen=true&utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def countingSort(arr):
    result = []
    value_counter = [0 for i in range(100)]

    for x in arr:
        value_counter[x] += 1

    for x in range(len(value_counter)):
        value = value_counter[x]

        if value != 0:
            result.extend([x] * value)

    return result

arr = [1,1,3,2,1]
print(countingSort(arr))