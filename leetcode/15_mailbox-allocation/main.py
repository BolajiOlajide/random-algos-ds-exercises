from math import floor

def minDistance(houses, k):
    no_of_houses = len(houses)
    if k > no_of_houses:
        return 0

    sorted_houses = sorted(houses)

    distance = [[0]*no_of_houses for i in range(no_of_houses)]

    for i in range(no_of_houses):
        for j in range(i, no_of_houses):
            if i == j:
                distance[i][j] = 0
            else:
                middle_idx = floor((i + j)/ 2)
                m = sorted_houses[middle_idx]

                for p in range(i, j+1):
                    distance[i][j] += abs(sorted_houses[p]-m)

    return dfs(sorted_houses, distance, 0, k, {})


def dfs(houses, distance, i, k, cache):
    no_of_houses = len(houses)

    if i == no_of_houses:
        return float("Inf")

    if k == 1:
        return distance[i][no_of_houses-1]

    min_dist = float("Inf")

    for j in range(i, no_of_houses):
        a = dfs(houses, distance, j+1, k-1, cache) if (j+1, k-1) not in cache else cache[(j+1, k-1)]
        min_dist = min(min_dist, a + distance[i][j])

    cache[(i, k)] = min_dist
    return min_dist


print(minDistance([1,4,8,10,20], 3))