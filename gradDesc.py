# Need starting theta values, alpha
# Use given partial derivatives, gradient vector grad-F

print "This will run gradient descent/ascent on a function F(x,y) from a given 2-D gradient"

# dplane = [(x,y), (x,y), (x,y)]
# theta[j] := theta[j]-alpha*(dF/dtheta)
def gradientDescent(dplane, theta, alpha, num_iters):
	m=len(dplane)
	J_History=tuple(0 for x in range(num_iters))


dplane = 


