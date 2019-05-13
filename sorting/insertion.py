# O(N**2). Good for partially sorted arrays
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while(j > 0 and nums[j] < nums[j-1]):
            swap(nums, j, j-1)
            j -= 1
    return nums

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]