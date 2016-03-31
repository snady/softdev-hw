UC_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LC_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NUMS = '1234567890'
ALPHANUMS = '. ? ! & # , ; : - _ *'

def validate(s):
	n_uc = len([ x for x in s if x in UC_LETTERS ])
	n_lc = len([ x for x in s if x in LC_LETTERS ])
	n_n = len([ x for x in s if x in NUMS ])
	n_an = len([ x for x in s if x in ALPHANUMS ])

	if n_uc > 0 and n_lc > 0 and n_n > 0:
		return True
	return False 
'''
1 point for each type of character
+ uppercase
+ lowercase
+ number
+ alphanum
1 point for multiple characters
+
+
+
1 point for multiple unique characters
+
+
+
'''
def strength(s):
	uc = [ x for x in s if x in UC_LETTERS ]
	lc = [ x for x in s if x in LC_LETTERS ]
	n = [ x for x in s if x in NUMS ]
	an = [ x for x in s if x in ALPHANUMS ]

	u_uc = set(uc)
	u_lc = set(lc)
	u_n = set(n)

	master = [uc,lc,n,an,uc,lc,n,u_uc,u_lc,u_n]

	strength = [ 1 for subl in master if len(subl) > 0 or len(subl) > 1 ]

	print sum(strength)


print strength('pasta')
print strength('HELLO PASTA')
print strength('Hello World111')
print strength('5343232')