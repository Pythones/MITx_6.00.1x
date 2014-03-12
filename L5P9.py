def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)



def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''

    #start grader
    intLenStr1 = len(str1)
    intLenStr2 = len(str2)

    #print str1 [1:intLenStr1]
    #print str2 [0:intLenStr2 - 1]

    #base case
    if intLenStr1 != intLenStr2: #not the same lenth
        return False
    elif intLenStr1 == 1 and str1 == str2: #final check!
        return True

   
    #recursive case
    elif str1 [0] == str2 [intLenStr2 - 1]: #first check in recursive cases
        return semordnilap(str1 [1:intLenStr1], str2 [0:intLenStr2 - 1])


    #end grader
print semordnilap("live", "evil")