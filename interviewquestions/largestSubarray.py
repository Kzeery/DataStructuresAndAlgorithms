def kadane_algorithm(nums):
    max_global, max_current = 0, 0

    for i in range(1, len(nums)):
        max_current = max(nums[i], nums[i] + max_current)

        if max_current > max_global:
            max_global = max_current
    
    return max_global