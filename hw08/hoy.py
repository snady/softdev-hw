import random

def inc(x):
	return x+1

def dec(x):
	return x-1

f = inc

flist = [inc,dec]

def makeAdder(n):
	def inner(x):
		return x+n
	return inner

add3 = makeAdder(3)
add5 = makeAdder(5)

def make_counter():
	count = [0]

	def inc():
		count[0]=count[0]+1
	def dec():
		count[0]=count[0]-1
	def reset():
		count[0]=0
	def get():
		return count[0]
	return {'inc':inc,'dec':dec,'reset':reset,'get':get}

c1 = make_counter()
#print c1['get']()
c1['inc']()
c1['inc']()
c1['inc']()
#print c1['get']()

def doubler(f):
	def inner():
		name = f()
		return name+name
	return inner

@doubler
def get_name():
	names = ['tom','sue','harry','lisa','sarah','horatio']
	return random.choice(names)

#TAKEAWAY
#you can write fxns that transforms fxns
#a python decorator is shorthand for calling a wrapper type function
#a python decorator encapsulates a closure
#a python decorator allows you to transparently wrap functionality