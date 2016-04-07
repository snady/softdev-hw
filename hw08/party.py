def pt(n):
	retL = []
	for a in range(n):
		for b in range(a+1,n):
			for c in range(b+1,n):
				if (a*a)+(b*b) == (c*c):
					retL.append([a,b,c])
	return retL

def pt2(n):
	return [ (a,b,c) for a in range(1,n) for b in range(a+1,n) for c in range(b+1,n) if (a*a)+(b*b)== (c*c) ]

print pt(5)
print pt(7)
print pt(15)

print pt2(5)
print pt2(7)
print pt2(15)

