
nums = [2,2,1,1,1,2,2]
temp = 1
maxOcc = 1
n = len(nums) / 2
# we can first sort the array, then check to see when it changes,
# add each iteration to temp, at the end when it switches see if temp is greater
# maxOcc then return maxOcc
nums.sort()
print(f"nums sorted: {nums}")
print(f"n = {n}")
for i in range(1, len(nums)):
    print(f"nums[{i}] = {nums[i]}")

    if (nums[i] == nums[i - 1]):
        print(f"    nums[{i}]: {nums[i]} == nums[{i-1}]: {nums[i-1]}")
        temp += 1
        print(f"    temp: {temp}")
        if (temp > n):
            print(f"        return nums[{i}] = {nums[i]} ")
    else:
        print(f"    nums[{i}]: {nums[i]} != nums[{i - 1}]: {nums[i - 1]}")
        temp = 1
        print(f"    temp: {temp}")
