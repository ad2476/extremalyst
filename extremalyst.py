# Need starting theta values, alpha
# Use given partial derivatives, gradient vector grad-F

# This will run gradient descent/ascent on a function F(x,y) from a given 2-D gradient

# dplane = [(x,y), (x,y), (x,y)]
# theta[j] := theta[j]-alpha*(dF/dtheta[j])
def gradientDescent(dplane, theta, alpha, num_iters):
	m=len(dplane)
	J_History=tuple(0 for x in range(num_iters))


print "Welcome to the extremalyst!\n"
print "Enter the components of a 2-D gradient vector, along with an initial theta-pair"
print "\t> A theta-pair is any point on the domain plane of the function F(x,y) in"
print "\t  the form (theta1, theta2)."
print "\t> The 2-D gradient vector consists of: gradF=<Fx, Fy>"

gradient = [raw_input("Fx :> ")]
gradient.append(raw_input("Fy :> "))

theta = [raw_input("theta1 :> ")]
theta.append(raw_input("theta2 :> "))

# Convert the gradient vector and theta-pair to 2-tuples
gradient = tuple(gradient)
theta = tuple(theta)

# DEBUGGING: print out gradient and theta-pair
print gradient
print theta

