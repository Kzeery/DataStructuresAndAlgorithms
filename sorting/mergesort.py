def mergeSort(nums):
    if len(nums)>1:
        mid = len(nums)//2
        lefthalf = nums[:mid]
        righthalf = nums[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nums[k]=lefthalf[i]
                i=i+1
            else:
                nums[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nums[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nums[k]=righthalf[j]
            j=j+1
            k=k+1
