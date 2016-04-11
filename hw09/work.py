import time

def timer(fn):
	def inner(arg):
		startTime = time.time()
		fnReturn = fn(arg)
		endTime = time.time()
		return "execution time: " + str(endTime-startTime) + "\n" + fnReturn
	return inner

def logger(fn):
	def inner(arg):
		return fn.func_name + '(' + str(arg) + ')' + "\n" + fn(arg)
	return inner 

@timer
@logger
def hello(n):
	return "hello"*n

hellow = hello(1)
hellow2 = hello(2)
hellow3 = hello(3)
print hellow
print hellow2
print hellow3