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
	def list(self):
		return self.storage

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
					pos+=1

				if (pos-i)!=0:
					token=comp[i:pos]
					output.append(token)
					[iterable.next() for x in xrange(1, pos-i)]
					continue
			except Exception, e:
				print e
				continue

			# If token is an operator, add to op_stack
			if token in OPERATORS:
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
			elif token in VARS: # It's a variable
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

# theta: (x,y)-point on domain plane
def eval(expression, theta):
	values=Stack()
	operands=[]

	# Substitute in variables from theta
	for i, token in enumerate(expression):
		if token==VARS[0]:
			expression[i]=theta[0]
		elif token==VARS[1]:
			expression[i]=theta[1]

	return expression

if __name__ == '__main__':
	import main