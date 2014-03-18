def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    #setting variables
    tplNew = ()
    Count = 0

    #setting the body
    for oddElements in aTup:
    	Count += 1
    	if Count % 2 == 0:
    		tplNew += (oddElements,)

    return tplNew
    

    #end grader
print oddTuples('I', 'am', 'a', 'test', 'tuple')