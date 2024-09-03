
nums = [1, 1, 1, 0]
target = -100
closest = 99999
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            print(f"{target} - ({nums[i]} + {nums[j]} + {nums[k]})")
            print(abs(target - (nums[i] + nums[j] + nums[k])))
            if abs(target - (nums[i] + nums[j] + nums[k])) < closest:
                closest = nums[i] + nums[j] + nums[k]
print(closest)

