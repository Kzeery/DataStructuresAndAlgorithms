# O(N**2) very slow
def selection_sort(nums):
    for i in range(len(nums)):
        mindex = i
        for j in range(i+1, len(nums)):
            if nums[mindex] > nums[j]:
                mindex = j
        if mindex != i:
            swap(nums, mindex, i)
    return nums

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

