import sys 
array = sys.stdin.read().split()
nums = [int(x) for x in array[1:]]
i = 0
idx = 0
for i in range(int(array[0])):
    n = nums[idx]
    k = nums[idx+1]
    idx +=2
    ar = nums[idx: idx+n]
    temp = ar.copy()
    temp.sort()
    # print(f"{temp=}")
    # print(f"{ar=}")
    if ar == temp or k >=2:
        print("YES")
    else:
        print("NO")
    idx += n
