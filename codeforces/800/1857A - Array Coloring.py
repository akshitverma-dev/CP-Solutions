import sys
array = sys.stdin.read().split()
total = int(array[0])
nums =  [int(x) for x in array[1:]]
idx = 0
for _ in range(total):
    n = nums[idx]
    ar = nums[idx+1:idx+1+n]
    odd = 0
    for i in ar:
        if i %2 != 0:
            odd +=1
    if odd%2==0:
        print("YES")
    else:
        print("NO")
    idx += 1+n