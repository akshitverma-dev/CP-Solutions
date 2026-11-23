import sys
ar = sys.stdin.read().split()
total_nums = int(ar[0])
i = 0
for i in range(total_nums):
    x = ar[(i*4)+3]
    s = ar[(i*4)+4]
    x_len = int(ar[(i*4)+1])
    s_len = int(ar[(i*4)+2])
    count = 0 
    if x_len >= s_len:
        if s in x:
            print(0)
        elif s in (x+x):
            print(1)
        else:
            print(-1)
    else:
        while len(x)< s_len:
            x += x
            count += 1
        if s in x:
            print(count)
        elif s in (x+x):
            print(count+1)
        else:
            print(-1)

