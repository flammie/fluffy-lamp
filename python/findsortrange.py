from math import ceil, floor


def searchRange(nums, target):
    delta = int(len(nums) / 2)
    if len(nums) == 1:
        if nums[0] == target:
            return [0,0]
        else:
            return [-1,-1]
    p = delta
    begin = -1
    end = -1
    while p >= 0 and p < len(nums):
        print(f"{p=} {delta=}")
        if nums[p] == target:
            begin = p
            end = p
            while p >= 0 and nums[p] == target:
                begin = p
                p = p - 1
            p = end
            while p < len(nums) and nums[p] == target:
                end = p
                p = p + 1
            break
        elif delta == 0:
            break
        elif nums[p] < target:
            p = p + int(ceil(delta / 2))
        elif nums[p] > target:
            p = p - int(ceil(delta / 2))
        delta = int(delta / 2)
    return [begin, end]


print(searchRange([1,3], 1))
print(searchRange([0,0,0,0,0,1,2,2,3,4,4,4,4,5,5,5,6], 6))
print(searchRange([0,1,2,3,4,4,4], 2))
