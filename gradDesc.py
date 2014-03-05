# Need starting theta values, alpha
# Use given partial derivatives, gradient vector grad-F
import shuntingYard
from shuntingYard import *

import sys

# F(x,y)=x*x*x+2*x+6*x*y-3*y*y
# grad-F=3*x*x+2+6*y, 6*x-6*y

# This will run gradient descent/ascent on a function F(x,y) from a given 2-D gradient
def computeCost(function, theta):
	try:
		return eval(function, theta)
	except OverflowError:
		return sys.float_info.max


# dplane = [(x,y), (x,y), (x,y)]
# theta[j] := theta[j]-alpha*(dF/dtheta[j])
def gradientDescent(gradient, coords, alpha, num_iters):
	grad=gradient[:]
	theta=coords[:]
	# Convert theta to float
	for i in xrange(len(theta)):
		theta[i]=float(theta[i])

	try:
		# 1. Compute partial derivatives (evaluate gradient at each theta step)
		# 2. Update both thetas simultaneously
		for i in xrange(num_iters):
			temp=[] # hold transitionary thetas
			dtheta=[eval(grad[0], theta), eval(grad[1], theta)]
			#print "\t"+str(dtheta)

			# Update theta simultaneously => hold transitional thetas in temp
			for j, theta_j in enumerate(theta):
				theta_j=theta_j - alpha*dtheta[j]
				temp.append(theta_j)

			theta=temp # update theta simultaneously
			#print theta # May want to disable this debugging since num_iters=1000...

		# Check for divergence, also round off theta to 5 decimal points
		for i in xrange(len(theta)):
			if theta[j]>1e10:
				print "Diverges (alpha="+str(alpha)+")"
				return tuple(theta)
			else:
				theta[i]=round(theta[i], 5)

		return tuple(theta)
	except OverflowError:
		print "OverflowError: Diverges (alpha="+str(alpha)+")"
		return (sys.float_info.max, sys.float_info.max)

if __name__ == '__main__':
	import main