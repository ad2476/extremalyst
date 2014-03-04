import shuntingYard
from shuntingYard import *

import gradDesc
from gradDesc import *

import os

# Extract comma-separated components, convert to tuple
def componify(vector):
	temp=""
	result=[]
	listignore=(" ", "<", ">", "(", ")")

	for item in vector:
		if item==",":
			result.append(temp)
			temp=""
		elif item in listignore:
			continue
		else:
			temp+=item

	result.append(temp)

	return tuple(result)

## --- EXECUTION BEGINS HERE --- ##
# 1. Prompt user for input        #
# 2. Set up raw gradient vector,  #
#    theta-pair                   #
# 3. Parse raw gradient vector    #

os.system("clear")

print "Welcome to the extremalyst! Calculate local minima!\n"
print "Enter the components of a 2-D gradient vector, along with an initial theta-pair"
print "\t> A theta-pair is any point on the domain plane of the function F(x,y) in"
print "\t  the form (theta1, theta2)."
print "\t> The 2-D gradient vector consists of: gradF=<Fx, Fy>"
print "\t> Be sure to explicitly state all multiplication (2x => 2*x)"

raw_gradient = raw_input("Gradient vector = ")
theta = raw_input("Theta-pair: ")
#raw_gradient.append(raw_input("Fy :> "))

raw_gradient = componify(raw_gradient)
theta = componify(theta)
print raw_gradient

#theta.append(raw_input("theta2 :> "))

# Convert the gradient vector and theta-pair to 2-tuples, parse gradient vector
gradient = shuntingYard(raw_gradient)

# DEBUGGING: Evaluate each component of the gradient
print "Substituting and evaluating..."
for comp in gradient:
	print eval(comp, theta)

print theta