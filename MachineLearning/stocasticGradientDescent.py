import numpy as np
import random
# ============== Modelling ===============
# points = [(np.array([2]), 4), (np.array([4]), 2)] # Feature vector, Expected output
# d = 2

# So we need a test case to see if the algorithm is working, so we begin by generating a weight vector and training data from the weight vector
true_weight = np.array([1,2,3,4,5])
points = []
d = len(true_weight)

for i in range(500000):
	x = np.random.randn(d)
	y = true_weight.dot(x) + np.random.randn() # We are adding noise to the y data just to see if the algorithm is working fine
	points.append((x, y))

def F(W, i): # Sum of squares for given slope
	x, y = points[i]
	return (W.dot(x) - y)**2

def dF(W, i): # Sum of squares for the derivative
	x, y = points[i]
	return 2 * (W.dot(x) - y) * x

# ============== Algorithm ================
def gradientDescent(F, dF, d, n): # Function, Derivative of the function and dimensionality
	W = np.zeros(d)
	eta = 1
	num_updates = 0

	for i in range(100):
		index = random.randint(0, n-1)
		for j in range(index): # So instead of finding the average of first index numbers, I am simply updating it index times
			value = F(W, j)
			derivative = dF(W, j)
			num_updates += 1
			eta = 1.0/num_updates
			W = W - eta * derivative
		print('Iteration: {}, W: {}, F(W): {}'.format(i, W, value))

gradientDescent(F, dF, d, len(points))
