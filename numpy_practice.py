import numpy as np_object

# utilization of some numpy functions
myList = [x for x in range(100)]
myArray = np_object.array(myList)  # convert a list to a numpy array
myArray = np_object.arange(0, 100, 10)  # similar to range (0, 100, 10)
# reshape myArray to a 2D array
# reshape doesn't change the array without reinitialization!!!!!
reshapedArray = myArray.reshape(2, 5)
reshapedArray = myArray.reshape(1, 10)
myArray = np_object.linspace(0, 100, 101)  # 0 to 100 by 101 steps
# myArray.resize(10, 10) # resize requires the array has its own data!


array1 = np_object.ones((3, 2))
array1 = np_object.vstack([array1, array1*2, array1*3])
array1 = np_object.vsplit(array1, 3)


array2 = np_object.array([2, 2**3])
print(array2.dtype)
array2 = array2.astype('f')
print(array2.dtype)

