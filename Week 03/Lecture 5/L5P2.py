def recurPower (base, exp):

	if exp == 0:
		return 1

	elif exp > 0:
		return base * recurPower (base, exp-1)

print recurPower (2, 4)