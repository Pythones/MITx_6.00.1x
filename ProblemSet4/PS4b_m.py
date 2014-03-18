def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line



def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    #start grader
    #repasa todas las letras de word y las comparas con los values de hand
    for char in word:
    	if hand.get (char, 0) != 0:  #si hay alguna igual, le restas 1 al value
    		hand[char] -= 1
    return hand  #devuelves hand revisado... pero ojo no se debe borrar el original (ESTO FALLA)

    #end grader

hand = {'a':1,'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
displayHand(hand)
print updateHand(hand, 'quail')