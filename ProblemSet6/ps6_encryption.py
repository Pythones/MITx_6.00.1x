# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    dict = {}

    for i in range (len(lowercase)):
       dict [lowercase[i]] = lowercase[(i+shift)%len(lowercase)]
       # %len() remapea el resultado y permite dar la vuelta al abecedario

    for i in range (len(uppercase)):
       dict [uppercase[i]] = uppercase[(i+shift)%len(uppercase)]

    #return "Not yet implemented." # Remove this comment when you code the function
    return dict



def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.

    cypherText = ""

    for char in text:

        if char in coder.keys():
            cypherChar = coder[char] #si char esta en el diccionario cifralo
        else:
            cypherChar = char #si char NO esta en el diccionario dejalo como estaba

        cypherText += cypherChar

    #return "Not yet implemented." # Remove this comment when you code the function
    return cypherText



def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.

    ans = buildCoder (shift)
    return applyCoder (text, ans)

    #return "Not yet implemented." # Remove this comment when you code the function


#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO

    #1. Set the maximum number of real words found to 0.
    #2. Set the best shift to 0.
    BestGuessShift = 0
    BestTry = 0

    #3. For each possible shift from 0 to 26:
    for i in range(26):

        #4. Shift the entire text by this shift.
        shiftText = applyShift(text,i)
        #print shiftText

        #5. Split the text up into a list of the individual words.
        listShiftText = shiftText.split(' ')
        #print listShiftText

        #6. Count the number of valid words in this list.
        Count = 0
        for word in listShiftText:
            if isWord(wordList, word) is True:
                Count += 1
            #print Count

        #7. If this number of valid words is more than the largest number of real words found, then:
        if Count > BestTry:

            #8. Record the number of valid words.
            BestTry = Count

            #9. Set the best shift to the current shift.
            BestGuessShift = i

        #10. Increment the current possible shift by 1. Repeat the loop starting at line 3.

    #11. Return the best shift.
    return BestGuessShift


    #return "Not yet implemented." # Remove this comment when you code the function

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.

    text = getStoryString()
    intKey = findBestShift(wordList, text)

    return applyShift(text, intKey)

    #return "Not yet implemented." # Remove this comment when you code the function






#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()

    #Test tries

    #print buildCoder(1)
    #print applyCoder("Hello, world!", buildCoder(3))
    #print applyCoder("Khoor, zruog!", buildCoder(23))
    #print applyShift('This is a test.', 8)
    #print applyShift('Bpqa qa i bmab.', 18)
    #print findBestShift(wordList, 'Pmttw, ewztl!')
    #print findBestShift(wordList, 'keykf lhZaze jwwbyv')
    print decryptStory()

    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'

    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()



