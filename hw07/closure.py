def repeat(s):
	return lambda n: s*n

r1 = repeat('hello')
r2 = repeat('goodbye')

'''
def r1(n):
	return repeat('hello')(n)

def r2(n):
	return repeat('goodbye')(n)

'''
print r1(2)
print r2(2)
print repeat('cool')(3)
