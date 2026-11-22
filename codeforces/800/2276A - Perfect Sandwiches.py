import sys
array = sys.stdin.read().split()
nums = [int(x) for x in array[1:]]
i = 0
while i <len(nums):
    if nums[i] <= nums[i+1]:
        print(-1)
    else:
        print(min(nums[i+1], nums[i]-nums[i+1]))
    i+=2