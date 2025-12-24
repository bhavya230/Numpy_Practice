import numpy as np
list=[1,2,3]
arr=np.array(list,dtype=int)
print(arr)
print(arr.shape)
list1=[2,3,4,5]
list2=[6,7,8,9]
arr1=np.array([list1,list2])
print(arr1)
print(arr1.shape)

# array indexing4
print(arr[::2])
print(arr1[0:1,1:3])