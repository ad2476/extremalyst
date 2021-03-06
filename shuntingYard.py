# The shunting yard and evaluation algorithm are based on a previous project,
# "Euler" (ad2476/Euler). Code in algExp.cpp.

import operator
import sys

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
		print "\t[STATUS] Parsing tokens..."
		comp=list(comp)

		output=[] # Sequence of constants and operators
		op_stack=Stack() # Working stack of operators
		i=0
		#print len(comp)
		while i < len(comp):
			token=comp[i]
			pos=i # position of last digit in token
			top=""
			#print i
			#print "Token: "+token
			#print "Comp: "+str(comp)
			#print "Output: "+str(output)
			#print "\tOp stack: "+str(op_stack.list())

			try:
				while pos<len(comp):
					if str.isdigit(comp[pos]) or comp[pos]==".": pos+=1
					else: break

				if (pos-i)!=0:
					token=top.join(comp[i:pos]) # top="" which is our separator
					#print "Token: "+token	
					#print "Pos: "+str(pos)

					output.append(token)
					if pos<len(comp) and (comp[pos] in VARS) or comp[pos]=="[": # Implied multiplication (e.g. '2x' or '2[x+1]')
						print "\t[INFO] Implied coef. multiplication assumed"
						comp.insert(pos, "*")
						#print str(comp)
					i+=pos-i
					continue
			except Exception, e:
				#print e
				i+=pos-i
				continue

			# If token is an operator, add to op_stack
			if token in OPERATORS:
				if not op_stack.empty():
					top=op_stack.top()

				if token=="-": # Is this subtraction or a negative symbol?
					if i==0 or comp[i-1]=="[": # Look behind
						print "\t[INFO] Negative number assumed"
						output.append("-1")
						op_stack.push("*")
						i+=1
						continue

				
				if token=="]":
					while not op_stack.empty():
						top=op_stack.pop()
						if top=="[":
							break

						output.append(top)

					try:
						if (comp[i+1] in VARS) or str.isdigit(comp[i+1]): # Implied multiplication (e.g. '[x+1]y')
							print "\t[INFO] Implied coef. multiplication assumed"
							op_stack.push("*")
					except IndexError, e:
						pass

					i+=1
					continue
				elif token=="[":
					pass
				elif PRECEDENCE[top]>=PRECEDENCE[token]:
					#print "Top: "+top
					while (not op_stack.empty()) and op_stack.top()!="[":
						top=op_stack.pop()

						if top!="[" and PRECEDENCE[top]>=PRECEDENCE[token]:
							output.append(top)
									
				op_stack.push(token)
				i+=1
				continue
			elif token==" ":
				i+=1
				continue
			elif token in VARS: # It's a variable
				output.append(token)

				try:
					if (comp[i+1] in VARS) or comp[i+1]=="[": # Implied multiplication (e.g. 'xy or x[1+y]')
						print "\t[INFO] Implied coef. multiplication assumed"
						op_stack.push("*")				
				except IndexError, e:
					pass
				i+=1
				continue

			print "\t[ERROR] UNEXPECTED OPERATOR: " + token
			i+=1

		# Pop remaining operators from stack:
		while not op_stack.empty():
			top=op_stack.pop()
			if (top=="[") or (top=="]"):
				print "\t[ERROR] BRACKET MISMATCH"
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
		elif token[0]=="-" and str.isdigit(list(token).pop()): # i.e. -2
			values.push(float(token))
		elif token in OPERATORS: # Otherwise it's an operator, evaluate
			if values.size()<2: # not enough values
				print "\t[ERROR] Insufficient values!"
				return [0]

			# Pop the two operands from the stack
			operands[1]=values.pop()
			operands[0]=values.pop()

			try:
				values.push(ops[token](operands[0], operands[1]))
			except (ValueError, ZeroDivisionError):
				print "\t[ERROR] Theta="+str(theta)+" passed out of domain"
				return sys.float_info.max
		else:
			print "\t[ERROR] Invalid operator: "+str(token)

	if values.size()==1:
		return values.pop()
	else:
		print "\t[ERROR] Value mismatch: "+str(values.list())

if __name__ == '__main__':
	import main