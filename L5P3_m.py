def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    #start grader

    if exp == 0:
        return 1

    elif exp > 0 and exp % 2 == 0:
    	return base * recurPowerNew (base^2, exp/2)

    elif exp > 0 and exp % 2 != 0:
		return base * recurPowerNew (base, exp-1)

    #end grader
print recurPowerNew (3, 4)

#FALLAAAAAAAAAAAAArg