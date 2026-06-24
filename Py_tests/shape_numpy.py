"""
1. In numpy, .shape will return a tuple with an entry for each dimension of the array.
Important: shape is not a method, but a property of Numpy arrays.
"""
"""
2. Testing if the array is a numpy array so that we have sure that we can use the shape property and
the return is a tuple
""" 
import numpy as np
a = np.array([1,2,3])
print(type(a))

"""
3. Why it returns a tuple? because a tuple is an immutable data structure, which means its perfect
to store structural metadata about the array."""


"""
4. The tuple will contain one entry per dimension"""
a = np.array([[1, 2, 4], [3, 7, 5]])
print(a.shape) # (2, 3) because we have 2 rows and 3 columns

"""
5. In ML, we treat a.shape[0] as the number of samples or the number of examples in a training set.
Generically, we treat like (number of training examples/samples, features,...), so when we have
a.shape[0] we'll have:"""
print(f"the number of training examples is: {a.shape[0]}") # 2 because we have 2 rows
#more complex example
arr = np.array([
    [[2, 3, 5], [3,4,6]], 
    [[5,6,7], [4,5,6]]])
print(f"arr.shape is: {arr.shape}")
"""
6. Intuition with different dimensions:
-1D array: (m, ) in which n is the number of elements in the array
"""
a1 = np.array([1, 2, 3])
print(f"1D array: a1.shape is {a1.shape}") # (3, ) because we have 3 elements in the array

"""
-2D array: (m, n) in which m is the number of rows/training examples and n is the number of features  
"""
a2 = np.array([[2,4,6], [5,6, 8]])
print(f"2D array: a2.shape is {a2.shape}") # (2, 3) because we have 2 rows and 3 columns

"""
7. If we want to check the dimension of the array, we can use the len() """
print(f"the dimension of a1 is: {len(a1.shape)}") # 1 because we have 1 entry in the shape tuple
print(f"the dimension of a2 is: {len(a2.shape)}") # 2 because we have 2 entries in the shape tuple

