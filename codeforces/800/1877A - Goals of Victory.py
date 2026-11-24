import sys 
ar = sys.stdin.read().split()
total = int(ar[0])
idx = 1
for i in range(total):
    teams = int(ar[idx])
    print(sum([int(x) for x in ar[idx+1:idx+teams]])*(-1))
    idx+=teams

