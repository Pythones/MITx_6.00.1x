def recurPowerNew (base, exp):
	if exp == 0:
		return base == 1
	elif exp > 0  and exp%2 == 0:
		return base * recurPowerNew ((base^2)^(exp/2), exp-1)

print recurPowerNew (2, 4)
#ESTE NO VAAAAA