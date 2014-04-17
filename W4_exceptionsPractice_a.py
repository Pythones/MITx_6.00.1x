def myLog(x, b):

	e = 0
	check = True

	while check:

		if(b**e <= x):
			e+=1
		else:
			check = False
			e -= 1

	return e


print myLog(9999,5)





