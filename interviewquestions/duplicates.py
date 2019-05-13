def duplicates(nums):
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print("Repitition found: ", abs(num))
