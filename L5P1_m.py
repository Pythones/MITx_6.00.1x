def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    #start grader

    if exp == 0: #base case
        result = 1
    else: #rest of cases
        result = 1
        while exp > 0:
            result = result * base
            exp -= 1

    return result

    #end grader
print iterPower(3, 3)