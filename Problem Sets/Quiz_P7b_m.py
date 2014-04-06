def McNuggets(n):

	def gcdRecur(a, b):
    	'''
	    a, b: positive integers
	    returns: a positive integer, the greatest common divisor of a & b.
	    '''
	    if b == 0:
	        return a

	    else:
	        return gcdRecur (b, a % b)

	Mc6 = 6
	Mc9 = 9
	Mc20 = 20

	#base cases
	if n%Mc6 == 0:
		return True
	elif n%Mc9 == 0:
		return True
	elif n%Mc20 == 0:
		return True

	#recursion cases
	elif n > 20:
		return McNuggets(n-20)
	elif n > 9:
		return McNuggets(n-9)
	elif n > 6:
		return McNuggets(n-6)

	else:
		return False

print McNuggets(133)