import sys 
ar = sys.stdin.read().split()
total = int(ar[0])
idx = 1
for i in range(total):
    n = int(ar[idx])
    k = int(ar[idx+1])
    nums = ar[idx+2:idx+2+n]
    if str(k) in nums:
        print("YES")
    else:
        print("NO")
    idx += 2+n

