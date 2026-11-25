import sys
array = sys.stdin.read().split()
total = int(array[0])
nums =  [int(x) for x in array[1:]]
idx = 0
for _ in range(total):
    ar = nums[idx: idx+3]
    Katie = ar[1]+(ar[2]//2)
    Anna = ar[0] + ar[2]-(ar[2]//2)
    if Katie>=Anna:
        print("Second")
    else:
        print("First")
    idx += 3
    