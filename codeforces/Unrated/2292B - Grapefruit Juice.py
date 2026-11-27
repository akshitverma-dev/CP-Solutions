import sys
ar = sys.stdin.read().split()
nums = [int(x) for x in ar[1:]]
total = int(ar[0])
idx = 0
for _ in range(total):
    length = nums[idx]
    no = nums[idx+1]
    joy = nums[idx+2]
    array = nums[idx+3:idx+3+length]
    array.sort()
    result = 0
    if length%no == 0:
        for i in range(length//no):
            try:
                if sum(array[i*no:(i*no)+no]) < joy:
                    result += joy
                else:
                    result += sum(array[i*no:(i*no)+no])
            except IndexError:
                result += sum(array[i*no:])
    else:
        for i in range((length//no) + 1):
            try:
                # temp = array[i*no:(i*no)+no]
                if sum(array[i*no:(i*no)+no]) < joy and len(array[i*no:(i*no)+no]) == no:
                    result += joy
                else:
                    result += sum(array[i*no:(i*no)+no])
            except IndexError:
                result += sum(array[i*no:])
    print(result)
    idx += 3+length