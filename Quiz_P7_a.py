def McNuggets(n):

	a6 = 6
	b9 = 9
	c20 = 20

	if n%a6 == 0:
		return True

	elif n%b9 == 0:
		return True

	elif n%c20 == 0:
		return True

	elif n > c20:
		return McNuggets(n-c20)

	elif n > b9:
		return McNuggets(n-b9)

	elif n > a6:
		return McNuggets(n-a6)

	else: return False


#print McNuggets(89)
