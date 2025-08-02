import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])

mul = np.multiply(arr1,arr2)
print("multiplied",mul)

#matrix multiplication
result = np.dot(arr1,arr2)
print (result)