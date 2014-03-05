# The shunting yard and evaluation algorithm are based on a previous project,
# "Euler" (ad2476/Euler). Code in algExp.cpp.
# NOTE: This very likely inherited a few of the bugs present in that algorithm,
# and may have introduced some new ones too... NEEDS TO BE THOROUGHLY TESTED

import operator

OPERATORS = ("[","]","^","*","/","+","-")
ops = {"^":operator.pow, "*":operator.mul, "/":operator.div, "+":operator.add, "-":operator.sub}
PRECEDENCE = {"[":4, "]":4, "^":3, "*":2, "/":2, "+":1, "-":1, "":0}
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
	def list(self):
		return self.storage
	def size(self):
		return len(self.storage)

# Based on ad2476/Euler: algexp.cpp
def shuntingYard(Inputted):
	raw_gradient=Inputted
	# Parsed gradient (list of lists)
	# gradient = [[shunting yard output 1], [output 2]]
	gradient = []

	# raw_gradient in form: (<string>, <string>)
	# Parse each <string> as its own algebraic expression
	for comp in raw_gradient:
		print "[STATUS] Parsing tokens..."

		output=[] # Sequence of constants and operators
		op_stack=Stack() # Working stack of operators
		top=""
		iterable=iter(xrange(len(comp)))
		for i in iterable:
			token=comp[i]
			pos=i # position of last digit in token
			try:
				while pos<len(comp) and (str.isdigit(comp[pos]) or comp[pos]=="."):
					pos+=1

				if (pos-i)!=0:
					token=comp[i:pos]
					output.append(token)
					if (comp[pos] in VARS) or comp[pos]=="[": # Implied multiplication (e.g. '2x' or '2[x+1]')
						print "[INFO] Implied coef. multiplication assumed"
						op_stack.push("*")
					[iterable.next() for x in xrange(1, pos-i)]
					continue
			except IndexError, e:
				continue

			# If token is an operator, add to op_stack
			if token in OPERATORS:
				if not op_stack.empty():
					top=op_stack.top()
				
				if token=="]":
					while not op_stack.empty():
						top=op_stack.pop()
						if top=="[":
							break

						output.append(top)

					try:
						if (comp[i+1] in VARS) or str.isdigit(comp[i+1]): # Implied multiplication (e.g. '[x+1]y')
							print "[INFO] Implied coef. multiplication assumed"
							op_stack.push("*")
					except IndexError, e:
						pass

					continue
				elif token=="[":
					pass
				elif PRECEDENCE[top]>PRECEDENCE[token]:
					op_stack.pop()
					if top!="[":
						output.append(top)
									
				op_stack.push(token)
				continue
			elif token==" ":
				continue
			elif token in VARS: # It's a variable
				output.append(token)

				try:
					if (comp[i+1] in VARS) or comp[i+1]=="[": # Implied multiplication (e.g. 'xy or x[1+y]')
						print "[INFO] Implied coef. multiplication assumed"
						op_stack.push("*")				
				except IndexError, e:
					pass
				continue

			print "[ERROR] UNEXPECTED OPERATOR: " + token

		# Pop remaining operators from stack:
		while not op_stack.empty():
			top=op_stack.pop()
			if (top=="[") or (top=="]"):
				print "[ERROR] BRACKET MISMATCH"
			output.append(top)

		gradient.append(output)

	return gradient

# theta: (x,y)-point on domain plane
def eval(inputted, coords):
	expression=inputted[:]
	theta=coords[:]
	values=Stack()
	operands=[0.0, 0.0]

	# Substitute in variables from theta
	for i, token in enumerate(expression):
		if token==VARS[0]:
			expression[i]=theta[0]
		elif token==VARS[1]:
			expression[i]=theta[1]

	# Parse tokens
	for token in expression:
		if type(token) is float: # If it's a number, add to stack of values
			values.push(token)
		elif str.isdigit(token[0]):
			values.push(float(token))
		elif token in OPERATORS: # Otherwise it's an operator, evaluate
			if values.size()<2: # not enough values
				print "[ERROR] Insufficient values!"
				return [0]

			# Pop the two operands from the stack
			operands[1]=values.pop()
			operands[0]=values.pop()

			values.push(ops[token](operands[0], operands[1]))
		else:
			print "[ERROR] Invalid operator: "+str(token)

	if values.size()==1:
		return values.pop()
	else:
		print "[ERROR] Value mismatch: "+str(values.list())

if __name__ == '__main__':
	import main