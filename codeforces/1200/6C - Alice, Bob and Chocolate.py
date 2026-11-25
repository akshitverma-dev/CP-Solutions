import sys
inp = sys.stdin.read().split()
ar = [int(x) for x in inp]
#ar = [6,1,4,7,3,2,1]
i = 1
counti = 1
j = ar[0]
countj = 1
for k in range(ar[0]):
  #print(ar)
  if len(ar) == 2:
    break
  if ar[i] < ar[j]:
    ar[j] = ar[j] - ar[i]
    ar[i] = 0
    
    if (i+1) != j:
      i+=1
      counti+=1
    else:
      break
  elif ar[i] > ar[j]:
    ar[i] = ar[i] - ar[j]
    ar[j] = 0
    
    if (j-1) != i:
      j-=1
      countj+=1
    else:
      break
  else:
    ar[j] = 0
    ar[i] = 0
    if (i+1) == j:
      break
    elif (i+2) == j:
      i+=1
      counti +=1
    else:
      i+=1
      counti +=1
      j-=1
      countj +=1
print(f"{counti} {(ar[0]-counti)}")
    
    
    
