#importing numpy 
import numpy as np

# 1D array
list=[1,2,3]
arr=np.array(list,dtype=int)
print(arr)
print(arr.shape)

# 2D array
list1=[2,3,4,5]
list2=[6,7,8,9]
arr1=np.array([list1,list2])
print(arr1)
print(arr1.shape)

# 3D array
list3=[10,11,12,13]
list4=[14,15,16,17]
arr2=np.array([
    [list1,list2],
    [list3,list4]
])
print(arr2)
print(arr2.shape)

# array indexing
print(arr[::2])
print(arr1[0:1,1:3])

# trying zeroes,ones functions
print(np.zeros((2,2),dtype=int)) 
print(np.ones((2,2),dtype=str))

# arange()

a=np.arange(10)
print(a)

#reshape()
a_new=a.reshape((2,5))
print(a_new)
print(a_new.base) # IT IS VIEW AS ORIGNAL ARRAY IS RETURED

print(np.arange(6).reshape(3,-1)) # detecting size of remaning 1 demionsion bi itself

#linspace()

b=np.linspace(1,10,5)
print(b)
