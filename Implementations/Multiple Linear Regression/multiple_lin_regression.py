#Here we will implement humble versions of Multiple linear regression
import numpy as np

"m: number of training examples"
"n: number of features"

#(1) create the model
"""
Our model will be expressed by a linear function with multiple variables. That means:
F(x) = W1*X1 + ... + Wn*Xn + b
"""
def model_prediction_v1(w, x, b):
    """
        ________________________________
        w: parameters (n,)
        x: features (n,)
        b: base value
        n: number of parameters/features
        ________________________________
        Returns b
    """
    n = w.shape[0]
    prediction = 0
    for i in range(n):
        prediction += w[i]*x[i]
    prediction += b
    return prediction

"""
Prediction model using dot product.
f(x) = w * x + b
*: dot product  
"""
def model_prediction_v2(w, x, b):
    """
        ________________________________
        w: parameters (n,)
        x: features (n,)
        b: base value
        ________________________________
        Returns b
    """
    prediction = np.dot(w,x) + b
    return prediction

#(2) cost function
"""
The cost function is expressed by: J(w, b) = 1/(2m)*SUM(f(x^i)-y^i)²
"""
def cost_function(x_train, w, targ, b):
    """
        ________________________________
        x: matrix of features (m, n)
        w: parameters (n,)
        targ: targets (m,)
        b: base value
        ________________________________
        Returns cost
    """
    num_examples = x_train.shape[0]
    constant = 1/(2*num_examples)
    squared_error = 0
    for i in range(num_examples): #summation
        squared_error += (model_prediction_v2(w, x_train[i], b) - targ[i])**2
    cost = constant * squared_error
    return cost



#(3) cost function derivative in respect to w
#(4) cost function derivative in respect to b


x_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
targets = np.array([460, 232, 178])

b = 785.1811367994083 #initial value of b
w = np.array([0.39133535, 18.75376741, -53.36032453, -26.42131618]) #initial values of w
print(f"w_init shape: {w.shape}, b_init type: {type(b)}")

#testing (1)
for i in range(x_train.shape[0]):
    prediction = model_prediction_v1(w, x_train[i, :], b)
    print(f"{i+1}º training example is: {x_train[i, :]} -> prediction: |{prediction:10}| ")
