def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''

    #start grader
    #base case
    if exp == 0:
        return 1


    #base case
	elif exp > 0 and exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)

    elif exp > 0 and exp % 2 != 0:
        return base * recurPowerNew(base, exp-1)


    #end grader
print recurPowerNew(2, 4)