import sys 
ar = sys.stdin.read().split()
nums = [int(x) for x in ar[1:]]
 
i = 0
while i < len(nums):
    n = nums[i]
    # print(f"{n=}")
    x = nums[i+1]
    # print(f"{x=}")
    # print(f"{i=}")
    maxi = 0
    cur = nums[i+2:i+2+n]
    # print(f"{cur=}")
    if len(cur) == 1:
        print(max(cur[0], (x-cur[0])*2))
    else:
        for j in range(len(cur)+1):
            # print(f"{nums[i+2:i+2+n]=}")
            # print(f"{x=}")
            if j==0:
                maxi = cur[j]
            elif j == len(cur):
                # print(f"{x=}")
                # print(f"{j=}")
                # print(f"{((x - cur[j-1])*2)=}")
                if maxi < (x - cur[j-1])*2:
                    maxi = (x - cur[j-1])*2
            else:
                if cur[j] - cur[j-1] > maxi:
                    maxi = cur[j] - cur[j-1]
            # print(f"{max=}")
        print(f"{maxi}")
    i+= (2 + n)