import sys
ar = sys.stdin.read().split()
total = int(ar[0])
idx = 1
for _ in range(total):
    nums = ar[idx]
    cur_str = ar[idx+1]
    freq = {}
    possible = False
    if len(cur_str) % 2 != 0:
        print("NO")
    else:
        if "0" in cur_str and "1" in cur_str:
            for i in range(len(cur_str)-2):
                if cur_str[i+1] == cur_str[i] or cur_str[i+1] == cur_str[i+2]:
                    possible = True
                    break
            if possible:
                print("YES")
            else:
                print("NO")
                    
        else:
            print("YES")
    idx+=2