import numpy as np
array1=list(map(int,(input().split())))
array2=list(map(int,(input().split())))
print(np.inner(array1,array2))
print(np.outer(array1,array2))

