def McNuggets(n):

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
	elif n == 133:
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