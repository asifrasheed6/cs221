# Modified version of Gradient Descent from Machine Learning Unit
import numpy as np
# ============== Modelling ===============
# points = [(np.array([2]), 4), (np.array([4]), 2)] # Feature vector, Expected output
# d = 2

# So we need a test case to see if the algorithm is working, so we begin by generating a weight vector and training data from the weight vector
true_weight = np.array([1,2,3,4,5])
points = []
d = len(true_weight)

for i in range(100000):
	x = np.random.randn(d)
	y = true_weight.dot(x) + np.random.randn() # We are adding noise to the y data just to see if the algorithm is working fine
	points.append((x, y))

def F(W): # Sum of squares for given slope
	return sum((W.dot(x) - y)**2 for x, y in points) / len(points)

def dF(W): # Sum of squares for the derivative
	return sum(2 * (W.dot(x) - y) * x for x, y in points) / len(points)

# ============== Algorithm ================
def gradientDescent(F, dF, d): # Function, Derivative of the function and dimensionality
	W = np.zeros(d)
	learning_rate = 0.01

	for i in range(100):
		value = F(W)
		derivative = dF(W)
		W = W - learning_rate * derivative
		print('Iteration: {}, W: {}, F(W): {}'.format(i, W, value))

gradientDescent(F, dF, d)
