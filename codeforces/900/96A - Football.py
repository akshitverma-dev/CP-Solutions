import sys
input_data = sys.stdin.read()
together = 1
max = 1
for i in range(len(input_data)-1):
    if input_data[i] == input_data[i+1]:
        together += 1
    else:
        if max < together:
            max = together
        together = 1
if max >= 7:
    print("YES")
else:
    print("NO")
    
    
    
    