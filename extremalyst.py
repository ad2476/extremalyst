# Need starting theta values, alpha
# Use given partial derivatives, gradient vector grad-F

# This will run gradient descent/ascent on a function F(x,y) from a given 2-D gradient

OPERATORS = [".", "(",")","^","*","/","+","-"]
PRECEDENCE = {".":5, "(":4, ")":4, "^":3, "*":2, "/":2, "+":1, "-":1, "":0}
VARS = ("x", "y")

class Stack:
	def __init__(self):
		self.storage = []
	def push(self, item):
		self.storage.append(item)
	def top(self):
		if self.storage:
			return self.storage[len(self.storage)-1]
	def pop(self):
		if self.storage:
			return self.storage.pop()
	def empty(self):
		return not self.storage
	def erase(self):
		del self.storage

# dplane = [(x,y), (x,y), (x,y)]
# theta[j] := theta[j]-alpha*(dF/dtheta[j])
def gradientDescent(grad, theta, alpha, num_iters):
	m=len(dplane)
	J_History=[]

# Based on ad2476/Euler: algexp.cpp
def shuntingYard(raw_gradient):
	# Parsed gradient (list of lists)
	# gradient = [[shunting yard output 1], [output 2]]
	gradient = []

	# raw_gradient in form: (<string>, <string>)
	# Parse each <string> as its own algebraic expression
	for comp in raw_gradient:
		print "Parsing tokens..."

		output=[] # Sequence of constants and operators
		op_stack=Stack() # Working stack of operators
		top=""
		iterable=iter(xrange(len(comp)))
		for i in iterable:
			token=comp[i]
			pos=i # position of last digit in token
			try:
				while pos<len(comp) and str.isdigit(comp[pos]):
					print pos
					pos+=1

				if (pos-i)!=0:
					token=comp[i:pos]
					output.append(token)
					[iterable.next() for x in range(pos-i)]
					continue
			except Exception, e:
				print e
				continue

			# If token is an operator, add to op_stack
			if OPERATORS.count(token):
				if not op_stack.empty():
					top=op_stack.top()
				
				if token==")":
					while not op_stack.empty():
						top=op_stack.pop()
						if top=="(":
							break

						output.append(top)
					continue
				elif token=="(":
					pass
				elif PRECEDENCE[top]>PRECEDENCE[token]:
					op_stack.pop()
					if top!="(":
						output.append(top)
									
				op_stack.push(token)
				continue
			elif token==" ":
				continue
			elif str.isalpha(token): # It's a variable
				if VARS.count(token):
					output.append(token)
				continue

			print "OP ERROR"

		# Pop remaining operators from stack:
		while not op_stack.empty():
			top=op_stack.pop()
			if (top=="(") or (top==")"):
				print "PARENS ERROR"
			output.append(top)

		gradient.append(output)

	return gradient


## --- EXECUTION BEGINS HERE --- ##
# 1. Prompt user for input        #
# 2. Set up raw gradient vector, theta-pair #

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

