nums = [0,1,2,2,3,0,4,2]
val = 2

print(nums)
temp = 0
for i in range(len(nums) - 1, -1, -1):
    print(i)
    if nums[i] == val:
        print(f"nums[{i}] == val")
        del nums[i]

print(nums)