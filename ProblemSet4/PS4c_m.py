
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    #print "  ", len(wordList), "words loaded."
    return wordList

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    #start grader

    #First test, is word made from hand?
    for char in word:
    	if hand.get (char, 0) != 0:  #si hay alguna igual, le restas 1 al value
    		hand[char] -= 1 #BUG! Re-testing last test to see if you mutate the original hand
    	elif hand.get (char, 0) == 0:  #si no hay igual mata
    		return False

    #Second test, is word in wordlist?
    if word in wordList:
    	return True
    else:
    	return False

    #end grader

#llamamos a wordlist
if __name__ == '__main__':
    wordList = loadWords()
#comprobamos nuestro codigo fresco del dia
hand = {'w':1,'d':1, 'e':1, 'm':1, 'u':1, 'i':1}
print isValidWord('weed', hand, wordList)