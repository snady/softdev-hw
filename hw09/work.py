import time

def timer(fn):
	startTime = time.time()
	return lambda: fn.func_name + ': '+ fn() + '\nexecution time: ' + str(time.time() - startTime)

@timer
def hello():
	return "Hi Friend\n" * 5

helloF = hello()
print helloF