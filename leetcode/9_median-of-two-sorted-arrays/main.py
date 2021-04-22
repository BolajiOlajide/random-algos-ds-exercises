from math import floor

def sort(arr1, arr2):
    result = []
    while (len(arr1)) and len(arr2):
        if arr1[0] <= arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))

    return [*result, *arr1, *arr2]


def findMedianSortedArrays(nums1, nums2):
    sorted_merged_array = sort(nums1, nums2)
    array_length = len(sorted_merged_array)

    if array_length % 2 == 0:
        half_index = int(array_length / 2)
        return (sorted_merged_array[half_index] + sorted_merged_array[half_index - 1]) / 2
    median_index = floor(array_length / 2)
    return sorted_merged_array[median_index]

print(findMedianSortedArrays([1,3], [2]))
print(findMedianSortedArrays([1,2], [3,4]))
print(findMedianSortedArrays([0,0], [0,0]))
print(findMedianSortedArrays([], [1]))
print(findMedianSortedArrays([2], []))

[0,1,2,4,5,6,8,9]