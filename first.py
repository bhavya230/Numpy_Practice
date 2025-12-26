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

# SLICING

# accesing 1D elements
print(arr[::2])

# accesing 2D elements
print(arr1[:,1])

# accesing 3d elements
print(arr2[:,:,2]) # all layers all rows 2 col (3rd col)

# Fancy Indexing

print(arr[[0,2]]) # 1D ARRAY
print(arr1[[0,1],[2,0]]) # 2D ARRAY
print(arr2[[0,1],[1,0],[2,3]]) # 3D ARRAY

# Boolean Indexing

print(arr1[arr1<5]) 

# Other Basic Operations 
print(arr*2)
print(arr**2)
print(arr+[2,3,4])


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

# copy vs view array

# copy array -- owns the data 
A=np.arange(5)
print(A)
B=A.copy()
B[1]=10
print(A)
print(B)

# view array--- dont owns the data
C=A.view()
C[1]=20
print(A)
print(C)

# Broadcasting

print(np.array([1,2,3]) +10)
print(np.array([1,2,3])+np.array([[1,2,3],[1,2,3]]))

# Array Iteration--simple

for x in np.nditer(arr):
    print(x)

for x in np.nditer(arr1):
    print(x)


for x in np.nditer(arr2):
    print(x)

# Array Iteration -- diff data types

for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print(x)

# Array Iteration -- diff step size

for x in np.nditer(arr1[:,::2]):
    print(x)

# Array Iteration -- with index 
for indx,x in np.ndenumerate(arr2):
    print(f"index: {indx} of {x}")