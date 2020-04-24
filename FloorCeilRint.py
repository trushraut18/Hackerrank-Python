import numpy 
arr1=[]
arr1.append(input().split())
arr1=numpy.array(arr1).astype(numpy.float)
numpy.set_printoptions(legacy='1.13')
print((numpy.floor(arr1).ravel()))
print((numpy.ceil(arr1).ravel()))
print((numpy.rint(arr1).ravel()))


