from functools import wraps
import time

def timer(fn):
    @wraps(fn)
    def inner(*args):
        startTime = time.time()
        fnReturn = fn(*args)
        endTime = time.time()
        print "execution time: " + str(endTime-startTime)
        return fnReturn
    return inner

def logger(fn):
    @wraps(fn)
    def inner(*args):
        print fn.func_name + '(' + str(args) + ')'
        return fn(*args)
    return inner
