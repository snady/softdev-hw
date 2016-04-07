def union(a,b):
	return a + [ x for x in b if x not in a ]
	#thanks sally
def intersect(a,b):
	return [ x for x in a for y in b if x == y]
def diff(a,b):
	return [ x for x in a if x not in b]
def symdiff(a,b):
	return union(diff(a,b),diff(b,a))
def carprod(a,b):
	return [ (x,y) for x in a for y in b ]

a = [1,2,3]
b = [2,3,4]

print union(a,b)
print intersect(a,b)
print diff(a,b)
print diff(b,a)
print symdiff(a,b)
print carprod([1,2],['red','white'])