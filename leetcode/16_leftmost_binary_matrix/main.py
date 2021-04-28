# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
from math import floor

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self, matrix = []):
        self.matrix = matrix

    def get(self, row, col):
        return self.matrix[row][col]

    def dimensions(self):
        return [len(self.matrix), len(self.matrix[0])]

# soln 1
# def leftMostColumnWithOne(binaryMatrix):
#     rows, cols = binaryMatrix.dimensions()

#     result = -1
#     current_row = 0
#     current_col = cols - 1

#     while (current_row < rows) and (current_col >= 0):
#         if binaryMatrix.get(current_row, current_col) == 1:
#             result = current_col
#             current_col -= 1
#         else:
#             current_row += 1

#     return result
max_possible_idx = 101

def matrix_binary_search(bm, row, no_of_cols):
    if bm.get(row, no_of_cols - 1) == 0:
        return max_possible_idx

    if bm.get(0, row) == 1:
        return 0

    min_idx = 0
    max_idx = no_of_cols - 1

    while (min_idx <= max_idx):
        mid = floor(min_idx + (max_idx - min_idx)/ 2)

        if (bm.get(row, mid) == 1):
            max_idx = mid - 1
        else:
            min_idx = mid + 1

    return min_idx

# soln 2
def leftMostColumnWithOne(binaryMatrix):
    rows, cols = binaryMatrix.dimensions()

    min_idx = max_possible_idx
    for i in range(rows):
        min_idx = min(min_idx, matrix_binary_search(binaryMatrix, i, cols))

    return min_idx


b = BinaryMatrix([[0, 0],[1,1]])
c = BinaryMatrix([[0,0,0,1],[0,0,1,1],[0,1,1,1]])

print(leftMostColumnWithOne(b), '<====') # 0
print(leftMostColumnWithOne(c), '<===') # 1