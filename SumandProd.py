import numpy as np
arr1=[]
n,m=map(int,input().split())
for i in range(n):
  for j in range(int(m/2)):
    arr1.append((input().split()))
arr1=np.array(arr1).astype(np.int)
print(np.prod((np.sum(arr1,axis=0))) )
    

