import numpy as np

print("The numpy version is: ", np.__version__)

zeroDarr = np.array(42) #this is )-D array

oneDarr = np.array([1,2,3,4,5,6,7]) #this is 1-D array

twoDarr = np.array([[1,2,3], [4,5,6]]) #this is 2-D array(used to represent matrix or 2nd order tensors)

threeDarr = np.array([[[1,2,3], [4,5,6]],[[7,8,9],[10,11,12]]])

#an array can have higher dimensions; when an array is created, you can define the d-number using ndmin arg.
dArr = np.array([1,2,3,4,5], ndmin=5)

# for arr in (zeroDarr, '\n', oneDarr, '\n', twoDarr, '\n', threeDarr, '\n', dArr):
#     print(arr)

#use the  numpy ndim attr to check array dimensions
# print('\n', threeDarr.ndim)

#Array indexing: to access a 2-D dimension array, we use comma separated integers representing the dimension and the index of the element
#use negative index(-1) to access array from the end
# print(twoDarr[0, 1])
# print(twoDarr[1, 2])
# print(twoDarr[1, -1])

#3-D
#use negative index(-1) to access array from the end
# print(threeDarr[0, 1, 2])
# print(threeDarr[1, 0, 0])
# print(threeDarr[0, 1, -2])

#slicing arrays: slicing in python means taking elements from one given index to another given index
# #this is an example of passing the start:end wihtout a step. note the end index will not be included when sliced
# print(oneDarr[1:5])
# print(oneDarr[3:])
# print(oneDarr[:4])
# print(oneDarr[-3:-1]) #use the minus operator to refer to an index from the end
# print(oneDarr[1:5:2]) #use the step value to determine the step of the slicing, the step is 1 by default
# print(oneDarr[::2]) #return every other element from the entire array with step not specifying start:end slice

#slicing 2-D
# print(twoDarr[1, 1:4])
# print(twoDarr[0:2, 2]) #return index 2 from both elements
# print(twoDarr[0:2, 1:4]) #slice index 1 to 4 from both elements

#datatypes in numpy
#use the optional argumnet in array() to specify a data type when creating an array
exDTarr = np.array([1,2,3,4,5], dtype='S')
# print(exDTarr)

#for i, u, f, S and U, we can define size as well
exISarr = np.array([1,2,3,4,5], dtype='i4')
# print(exISarr)