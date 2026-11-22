import sys 
ar = sys.stdin.read().split()
nums = [int(x) for x in ar[1:]]
i = 0 
while i < len(nums):
    n = nums[i]
    test = nums[i+1:i+1+n]
    if test[0] == min(test):
        print("YES")
    else:
        print("NO")
    i += (n+1)