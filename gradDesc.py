# Need starting theta values, alpha
# Use given partial derivatives, gradient vector grad-F
import shuntingYard
from shuntingYard import *

# This will run gradient descent/ascent on a function F(x,y) from a given 2-D gradient

# dplane = [(x,y), (x,y), (x,y)]
# theta[j] := theta[j]-alpha*(dF/dtheta[j])
def gradientDescent(gradient, coords, alpha, num_iters):
	grad=gradient[:]
	theta=coords[:]
	# Convert theta to float
	for i in xrange(len(theta)):
		theta[i]=float(theta[i])

	# 1. Compute partial derivatives (evaluate gradient at each theta step)
	# 2. Update both thetas simultaneously
	for i in xrange(num_iters):
		temp=[] # hold transitionary thetas
		dtheta=[eval(grad[0], theta), eval(grad[1], theta)]

		# Update theta simultaneously => hold transitional thetas in temp
		for j, theta_j in enumerate(theta):
			theta_j=theta_j - alpha*dtheta[j]
			temp.append(theta_j)

		theta=temp # update theta simultaneously
		#print theta # May want to disable this debugging since num_iters=1000...

	# Round off theta to 5 decimal points
	for i in xrange(len(theta)):
		theta[i]=round(theta[i], 5)

	return tuple(theta)

if __name__ == '__main__':
	import main