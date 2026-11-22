import sys 
ar = sys.stdin.read().split()
i = 0
while i < len(ar)-1:
    num = int(ar[1+i])
    test = ar[i+2]
    count = 0
    more = True
    for k in range(len(test)):
        if k <= len(test)-3:
            if test[k] == test[k+1] and test[k] == test[k+2] and test[k] == '.':
                print(2)
                more = False
                break
            else:
                if test[k] == '.':
                    count+=1
        elif test[k] == '.':
            count += 1
    if more:
        print(count)
    i += 2