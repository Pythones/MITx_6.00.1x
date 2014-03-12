def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #start grader
    intMid = len(aStr)/2
    strMir = aStr[intMid:(intMid+1)]
    #print aStr[(intMid):]

    #base case
    if len(aStr) == 0: #empty string returns false
        return False
    elif len(aStr) == 1: #this line is the clue!
        if char == aStr:
            return True
        else:
            return False
    elif char == aStr[intMid:(intMid+1)]: #just in case we are lucky
        return True
   
    #recursive case
    elif char > strMir: #looking 
        return isIn(char, aStr[(intMid):])
    elif char < strMir:
        return isIn(char, aStr[:(intMid)])
    
    #end grader
print isIn('h', 'lq')