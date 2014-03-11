def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    #start grader
    if b == 0:
    	return a

    else:
    	return gcdRecur (b, a % b) #Euclids rules!

    #end grader
print gcdRecur (9, 12)