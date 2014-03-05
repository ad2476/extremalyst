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

	return result

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
print "\t> Be sure vector components and coordinate pairs are comma-separated!"
print "\t> Use brackets '[ ]' instead of parentheses '( )' within expressions!"

raw_function = raw_input("[PROMPT] F(x,y) = ")

if raw_function=="quit":
	quit()

function = shuntingYard([raw_function, ""])
function = function[0] # remove the trailing "" list produced by shuntingYard()
print function

raw_gradient = raw_input("[PROMPT] Gradient vector = ")

theta = raw_input("[PROMPT] Theta-pair: ")

raw_gradient = componify(raw_gradient)
theta = componify(theta)

if len(raw_gradient)!=2 or len(theta)!=2:
	print "[ERROR] Check entered gradient vector or theta-pair"
	quit()

print raw_gradient,
print theta

# Convert the gradient vector and theta-pair to 2-tuples, parse gradient vector
gradient = shuntingYard(raw_gradient)

print gradient

# DEBUGGING: Evaluate each component of the gradient
print "[STATUS] Substituting and evaluating..."
print "Initial gradient: ",
for comp in gradient:
	print str(eval(comp, theta)) + " ",
print "\nF"+str(tuple(theta))+" = "+str(eval(function, theta))

descent = gradientDescent(gradient, theta, 0.01, 1000)
ascent = gradientDescent(gradient, theta, -0.01, 1000)
if eval(function, descent)<eval(function, ascent):
	print "\n\n\nGRADIENT DESCENT RESULTS:"
	print descent
else:
	print "\n\n\nGRADIENT ASCENT RESULTS:"
	print ascent