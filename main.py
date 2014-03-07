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

if os.name=='posix':
	os.system("clear")

print "Welcome to the extremalyst! Calculate local extrema!\n"
print "Enter the components of a 2-D gradient vector, along with an initial theta-pair"
print "\t> A theta-pair is any point on the domain plane of the function F(x,y) in"
print "\t  the form (theta1, theta2)."
print "\t> Be sure vector components and coordinate pairs are comma-separated!"
print "\t> Use brackets '[ ]' instead of parentheses '( )' within expressions!"
print "\t> For more information and usage help, see README"

raw_function = raw_input("[PROMPT] F(x,y) = ")

if raw_function=="quit":
	quit()
elif raw_function=="pass":
	function=["0"]
else:
	function = shuntingYard([raw_function, ""])
	function = function[0] # remove the trailing "" list produced by shuntingYard()

#print function

raw_gradient = raw_input("[PROMPT] Gradient vector = ")

theta = raw_input("[PROMPT] Theta-pair: ")

raw_gradient = componify(raw_gradient)
theta = componify(theta)

if len(raw_gradient)!=2 or len(theta)!=2:
	print "\t[ERROR] Check entered gradient vector or theta-pair"
	quit()

#print raw_gradient,
#print theta

# Convert the gradient vector and theta-pair to 2-tuples, parse gradient vector
gradient = shuntingYard(raw_gradient)

#print gradient

# DEBUGGING: Evaluate each component of the gradient
print "\t[STATUS] Substituting and evaluating..."
print "\nInitial gradient: ",
for comp in gradient:
	print str(eval(comp, theta)) + " ",
print "\nF"+str(tuple(theta))+" = "+str(eval(function, theta))

descent = gradientDescent(gradient, theta, 0.01, 10000)
ascent = gradientDescent(gradient, theta, -0.01, 10000)

print "\n------------------------"
print "\nGRADIENT DESCENT RESULTS:"
dcost=computeCost(function,descent)
print "F"+str(descent)+" = "+str(dcost)

print "\nGRADIENT ASCENT RESULTS:"
acost=computeCost(function,ascent)
print "F"+str(ascent)+" = "+str(acost)+"\n"

largetheta=(1e10, 1e10)
if ascent==descent:
    print "Note: This is likely a saddle point!"
if sum(ascent)>=sum(largetheta) and sum(descent)<=sum(largetheta): # Ascent diverged, descent converged
	print "There exists a local minimum at "+str(descent)
elif sum(ascent)<=sum(largetheta) and sum(descent)>=sum(largetheta): # Ascent converged, descent diverged
	print "There exists a local minimum at "+str(descent)
