def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''

    #start grader

	return 1 + lenRecur (aStr[1:]) #hard to imagine that 'return 1 +' will work

    return

	#end grader
	
print lenRecur ("locos")