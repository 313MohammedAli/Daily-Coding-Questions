nums1 = [0]
m = 0
nums2 = [1]
n = 1

"""
ATTEMPT 1
def moveRight(nums1, loc, m):
    # Iterate from m to loc
    for i in range(m, loc, -1):
        nums1[i] = nums1[i - 1]
    return nums1

for i in range(n):
    print(f"i: {i}")
    print(nums1)
    if(m == 0):
        nums1[0] = nums2[0]

    if (nums2[i] > nums1[i]):
        print(f"nums2[i] ({nums2[i]}) greater than nums1[i] ({nums1[i]})")

        for x in range(i + 1, m+n):
            print(f"nums1[x] = {nums1[x]}, x = {x}")
            if (nums2[i] < nums1[x]):
                moveRight(nums1, x, m)
                nums1[x] = nums2[i]
                break
            if(nums1[x] == 0):
                nums1[x] = nums2[i]
            if (x == m+n - 1):
                print("reached the end of nums1")
                nums1[x] = nums2[i]

    if (nums2[i] <= nums1[i]):
        print(f"nums2[i] ({nums2[i]}) less than than nums1[i] ({nums1[i]}")
        moveRight(nums1, i, m)
        nums1[i] = nums2[i]
"""  # Attempt 1

# Attempt 2
# This time start from the end of the loop and move backwards
for i in range(n-1, -1, -1):
    print(f"nums2[{i}] = {nums2[i]}")
    # we are starting at the last place in nums2 array
    # want to check that agaisnt the last place in nums 3 array
    for x in range(m-1, -1, -1):
        print(f"    nums1[{x}] = {nums1[x]}")
        # first check to see if last position of nums 2 is bigger
        if(nums2[i] > nums1[x]):
            print(f"    nums2[i] > nums1[x]")
            nums1[m+i] = nums2[i]
            print(f"    nums1 = {nums1}")
            break
        # then check if theyre the same
        if(nums2[i] == nums1[x]):
            print(f"    nums2[i] == nums1[x]")
            nums1[x + 2] = nums1[x+1]
            nums1[x+1] = nums2[i]
            print(f"    nums1 = {nums1}")
            break

print(nums1)
