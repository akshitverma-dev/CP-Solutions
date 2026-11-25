import sys
array = sys.stdin.read().split()
total = int(array[0])
nums =  [int(x) for x in array[1:]]
idx = 0
for _ in range(total):
    n = nums[idx]
    ar = nums[idx+1: idx+1+n]
    b = []
    c = []
    maxi = max(ar)
    mini = min(ar)
    if maxi == mini:
        print(-1)
    else:
        for i in ar:
            if i == maxi:
                c.append(i)
            else:
                b.append(i)
        print(f"{len(b)} {len(c)}")
        print(*b)
        print(*c)
    idx += 1+n