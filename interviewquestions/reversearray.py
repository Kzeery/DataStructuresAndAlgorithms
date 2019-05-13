def reverseArray(nums):
    for x in range(len(nums)//2):
        nums[x], nums[-1 - x] = nums[-1 - x], nums[x]
    return nums

print(reverseArray([1,2,3,4,5]))