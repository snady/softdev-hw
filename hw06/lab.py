UC_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LC_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NUMS = '1234567890'
ALPHANUMS = '.?!&#,;:-_*'

'''
Checks if password meets the minimum criteria of:
At least 1 uppercase character
At least 1 lowercase character
At least 1 number
'''
def validate(s):
	n_uc = len([ x for x in s if x in UC_LETTERS ])
	n_lc = len([ x for x in s if x in LC_LETTERS ])
	n_n = len([ x for x in s if x in NUMS ])

	if n_uc > 0 and n_lc > 0 and n_n > 0:
		return True
	return False 
'''
Password Strength Rating Scale (1 - 10)
+ 1 point for each character type (upper, lower, num, alphanum)
e.x Hi 5 = 3 points
+ 1 point for multiple characters of each type
e.x HiHi 55 = 6 points
+ 1 point for multiple unique characters of each type 
e.x Hello World 51 = 9 points
e.x Wh3r3_1s_Th3_Sp4gh3tt1? = 10 points
'''
def strength(s):
	uc = [ x for x in s if x in UC_LETTERS ]
	lc = [ x for x in s if x in LC_LETTERS ]
	n = [ x for x in s if x in NUMS ]
	an = [ x for x in s if x in ALPHANUMS ]

	u_uc = set(uc)
	u_lc = set(lc)
	u_n = set(n)

	master1 = [uc,lc,n,an]
	master2 = [uc,lc,n,u_uc,u_lc,u_n]
	strength = [ 1 for subl in master1 if len(subl) > 0 ] + [ 1 for subl in master2 if len(subl) > 1 ]

	return sum(strength)


#print strength('pasta')
#print strength('HELLO PASTA')
#print strength('Hello World111')
#print strength('5343232')