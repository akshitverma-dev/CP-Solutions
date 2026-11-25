import sys
ar = sys.stdin.read().split()
nums = [int(x) for x in ar[1:]]
total = int(ar[0])
idx = 0
for _ in range(total):
    n = nums[idx]
    array = nums[idx+1:idx+n+1]
    result = [nums[idx+1]]

    for i in range(1,len(array)):
        if max(array[i],array[i-1]) == array[i]:
            result.append(array[i])
        else:
            result.append(array[i])
            result.append(array[i])
    print(len(result))
    print(*result)
    idx += 1+n