# O(N**2) very slow
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                swap(nums, j, j+1)
    
    return nums

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]
