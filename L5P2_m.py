def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    #start grader

    if exp == 0:
        return 1

    elif exp > 0:
        return base * recurPower (base, exp-1)

    #end grader
print recurPower (3, 3)