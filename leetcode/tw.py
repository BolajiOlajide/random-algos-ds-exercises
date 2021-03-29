def twoSum(nums, target):
    for x in range(len(nums)):
        for y in nums.po
        if (nums[x] + nums[x+1]) == target:
            return [x, x+1]

print(twoSum([3,2,3], 6))