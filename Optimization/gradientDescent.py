# To minimize the Least Square with the help of Gradient Descent for the given data points
points = [(2, 4), (4, 2)]

def F(W): # Sum of squares for given slope
	return sum(((W*x) - y)**2 for x, y in points)

def dF(W): # Sum of squares for the derivative
	return sum(2 * ((W*x) - y) * x for x, y in points)

W = 0
learning_rate = 0.1

for i in range(100):
	value = F(W)
	derivative = dF(W)
	W -= learning_rate * derivative
	print('Iteration: {}, W: {}, dF(W): {}'.format(i, W, derivative))
