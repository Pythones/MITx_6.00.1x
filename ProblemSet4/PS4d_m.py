def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """

    ans = 0

    lista = hand.values()
    for index in lista:
    	ans += index

    return ans


hand = {'a':1,'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
print calculateHandlen(hand)