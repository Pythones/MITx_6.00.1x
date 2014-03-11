def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    #start grader
    intMin = min (a, b) #find the minimun

    while intMin > 0: #starting the loop

    	if a % intMin == 0 and b % intMin == 0:
    		return intMin

    	else: #if first condition fail, we reduce by one and try again
    		intMin -= 1

    #end grader
print gcdIter (17, 12)