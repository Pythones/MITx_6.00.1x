def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return (out += s2)
        if s2 == '':
            return (out += s1)
        else:
            #PLACE A LINE OF CODE HERE
    return helpLaceStrings(s1, s2, '')