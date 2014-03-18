SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    #start grader
    ans1 = 0

    #The score for the hand is the sum of the scores for each word formed
    for char in word:
        ans1 += SCRABBLE_LETTER_VALUES[char]
    #print ans1  #internal test 01
            
    #The score for a word is the sum of the points for letters in the word, multiplied by the length of the word,
    ans2 = ans1 * len(word)
    #print ans2 #internal test 02

    #plus 50 points if all n letters are used on the first word created.
    if len(word) == n:
        ans3 = ans2 + 50
    else:
        ans3 = ans2

    return ans3  #final output
    #end grader

print getWordScore('weed', 4)