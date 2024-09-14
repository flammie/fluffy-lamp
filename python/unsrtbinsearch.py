from math import ceil, floor


def search(nums, target):
    if target == nums[0]:
        return 0
    elif target == nums[-1]:
        return len(nums) - 1
    delta = int(floor(len(nums) / 2))
    p = delta
    i = nums[p]
    while i != target:
        if delta < 1:
            break
        elif p < 0 or p > len(nums):
            return -1
        delta = int(ceil(delta / 2))
        print(f"{target=}, {i=}, {p=}, {delta=}")
        if i < target:
            if nums[p + delta] < nums[p]:
                # we'll hit the pivot
                if nums[p + 2*delta - 1] >= target:
                    p = p + delta
                    i = nums[p]
                else:
                    p = len(nums) - delta
                    i = nums[p]
            else:
                p = p + delta
                i = nums[p]
        elif i > target:
            if nums[p - delta] > nums[p]:
                # we'll hit the pivot
                if nums[p - 2*delta] <= target:
                    p = p - delta
                    i = nums[p]
                else:
                    p = delta
                    i = nums[p]
            else:
                p = p - delta
                i = nums[p]
        else:
            return p
    if i != target:
        return -1
    else:
        return p


print(search([4, 5, 6, 7, 0, 1, 2], 0))
