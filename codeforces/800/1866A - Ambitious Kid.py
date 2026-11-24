import sys
ar = sys.stdin.read().split()
nums = [abs(int(x)) for x in ar[1:]]
print(min(nums))