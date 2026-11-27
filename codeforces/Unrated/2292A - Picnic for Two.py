import sys 
ar = sys.stdin.read().split()
nums = [int(x) for x in ar[1:]]
numbers = int(ar[0])
idx = 0
for i in range(numbers):
    slice = nums[idx]
    num_a = []
    num_b = []
    a = nums[idx+1]
    b = nums[idx+2]
    k = a % slice
    n = 1
    result = 0
    while k not in num_a:
        num_a.append(k)
        n+=1
        k = (n*a)%slice
    j = b % slice
    n = 1
    while j not in num_b:
        num_b.append(j)
        if j in num_a:
            result += 1
        n+=1
        j = (n*b)%slice

    print(result)
    idx += 3