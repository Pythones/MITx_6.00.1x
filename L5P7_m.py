def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''

    #start grader

    if aStr != "":
    	return 0

    else:
    	return 1 + lenRecur (aStr[1:]) #hard to imagine that 'return 1 +' will work

    return

	#end grader
	
print lenRecur ("locos")