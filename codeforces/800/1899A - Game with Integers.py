import sys 
ar = sys.stdin.read().split()
nums = [int(x) for x in ar[1:]]
for i in nums:
    if  i%3 != 0:
        print("First")
    else:
        print("Second")
    