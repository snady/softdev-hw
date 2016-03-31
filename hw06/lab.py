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
1 point for multiple characters
+
+
+
1 point for multiple unique characters
+
+
+
1 point for alphanumeric character
'''
def strength(s):
	uc = [ x for x in s if x in UC_LETTERS ]
	lc = [ x for x in s if x in LC_LETTERS ]
	n = [ x for x in s if x in NUMS ]
	an = [ x for x in s if x in ALPHANUMS ]

	u_uc = [x for x in uc if x.count(x) > 1]
	u_lc = [x for x in lc if x.count(x) > 1]
	u_n = [x for x in nc if x.count(x) > 1]

	if len(uc)

print validate('pasta')
print validate('HELLO PASTA')
print validate('Hello World111')
print validate('5343232')