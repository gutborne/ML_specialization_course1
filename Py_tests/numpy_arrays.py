import numpy as np
"np.zeros() is a function in the NumPy library that creates an array filled with zeros."
" The argument passed to np.zeros() specifies the shape of the array. "
"For example, np.zeros(3) creates a 1D array with 3 elements, all initialized to zero. "
"Similarly, np.zeros((3,)) also creates a 1D array with 3 elements, all initialized to zero. "
"The output of both commands will be the same: [0. 0. 0.]."
a = np.zeros(3); print(a); # [0. 0. 0.]
a = np.zeros((3,)); print(a) # [0. 0. 0.]
a = np.zeros((3, 4)); print(a) # a 2D array with 3 rows and 4 columns, all initialized to zero.
"np.random.random_sample() is a function in the NumPy library that generates random "
"numbers between 0 and 1. Note that it accepts a tuple as an argument to specify the shape of "
"the output array. "
a = np.random.random_sample((3, 4 )); print(a)

"np.arange() is a function in the NumPy library that creates an array with a range of values. "
"The argument passed to np.arange() specifies the end value of the range. "
"Note that bellow we have a = np.arange(6.3) which means that we want to create an array with values"
"from 0 to 6.3 (exclusive) with a step of 1, that means that the output will be [0. 1. 2. 3. 4. 5. 6.]"
"because the end value is exclusive and the step is 1 by default. In the end we will have an array with 7"
" elements, starting from 0 and ending at 6 (exclusive)."
a = np.arange(6.3); print(a); print(a.shape)
a = np.arange(10, 20); print(a); print(a.shape)
a = np.arange(4); print(a) 
"np.random.rand() is a function in the NumPy library that generates random numbers between 0 and 1. "
a = np.random.rand(4); print(a)
"note that both np.random.random.rand() and np.arange() dont accept a tuple as an argument."

a = np.array([1, 5, 6]); print(f"{a} {a.shape} {a.dtype}")
