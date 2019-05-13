from random import shuffle
def quick_sort(nums):
    shuffle(nums)
    return quicksort(nums, 0, len(nums) - 1)

def quicksort(nums, low, high):
    if low >= high:
        return
    if high - low < 8:
        return insertion_sort(nums, low, high)
    pivot_index = partition(nums, low, high)
    quicksort(nums, low, pivot_index -1)
    quicksort(nums, pivot_index +1, high)

def partition(nums, low, high):
    pivot_index = (low+high)//2
    swap(nums, pivot_index, high)

    i = low

    for j in range(low, high):
        if nums[j] <= nums[high]:
            swap(nums, i, j)
            i += 1
    swap(nums, i, high)

    return i

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def insertion_sort(nums, low, high):
    for i in range(low+1, high + 1):
        j = i
        while(j > low and nums[j] < nums[j-1]):
            swap(nums, j, j-1)
            j -= 1
    return nums

def createList(num):
    from random import randint
    a = []
    for x in range(num):
        a.append(randint(0, num))
    return a