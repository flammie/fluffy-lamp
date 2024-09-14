from math import ceil, floor


def searchInsert(nums, target):
    delta = int(len(nums) / 2)
    p = delta
    while 0 <= p < len(nums):
        if nums[p] == target:
            return p
        elif delta == 0:
            break
        elif nums[p] < target:
            p = p + int(ceil(delta / 2))
        elif nums[p] > target:
            p = p - int(ceil(delta / 2))
        delta = int(delta / 2)
    if p >= len(nums):
        return len(nums)
    elif p < 0:
        return 0
    elif nums[p] < target:
        return p + 1
    else:
        return p


print(searchInsert([1, 3, 5, 6], 2))
