import shuntingYard
from shuntingYard import *

import gradDesc
from gradDesc import *

import os

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

gradient = [raw_input("Fx :> ")]
gradient.append(raw_input("Fy :> "))

theta = [raw_input("theta1 :> ")]
theta.append(raw_input("theta2 :> "))

# Convert the gradient vector and theta-pair to 2-tuples
gradient = tuple(gradient)
theta = tuple(theta)

# DEBUGGING: print out gradient and theta-pair
print shuntingYard(gradient)
print theta