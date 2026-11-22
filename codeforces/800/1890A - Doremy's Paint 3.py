import sys 
ar = sys.stdin.read().split()
nums = [int(x) for x in ar[1:]]
i = 0 
while i < len(nums):
    n = nums[i]
    temp = nums[i+1:i+1+n]
    fre = {}
    for j in temp:
        if j not in fre:
            fre[j] = 1
        else:
            fre[j] += 1
    keys = list(fre)
    # print(keys)
    # print(fre)
    if len(keys)!=2 and len(keys)!=1:
        print("NO")
    else:
        if len(keys) == 1:
            print("YES")
        elif abs(fre[keys[0]] - fre[keys[1]]) == 1 or abs(fre[keys[0]] - fre[keys[1]]) == 0 :
            print("YES")
        else:
            print("NO")
    i += (1+n)