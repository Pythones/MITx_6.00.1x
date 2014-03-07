a = 2
b = 999

def iterPower(base,exp):
	
	if exp == 0:
		result = 1
	elif exp == 1:
		result = base
	else:
		result = base
		for i in range(exp-1):
			result *= base

	return result

print iterPower(a,b)
