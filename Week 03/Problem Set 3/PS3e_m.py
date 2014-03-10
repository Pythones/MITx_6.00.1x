#secretWord = "locos"

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """

    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    
    dblLenthA = len(secretWord)
    dblLenthB = len(lettersGuessed)
    intCount = 0

    for i in range (dblLenthA):
        for j in range (dblLenthB):
            if secretWord [i] == lettersGuessed [j]:
                intCount += 1
                break

    if intCount == dblLenthA:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''

    intCount = 0
    strGuess = ""

    for char in secretWord:

        if char in lettersGuessed:
            strGuess += char + " "
        else:
            strGuess += "_ "

    return strGuess

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    
    strAbc = string.ascii_lowercase
    strGuess = ""

    for char in strAbc:
        if char in lettersGuessed:
            strGuess += ""
        else:
            strGuess += char

    return strGuess

def hangman(secretWord):

	#grader - start
    intLenWord = len(secretWord)
    numGuesses = 8
    adivinadas = ""
     
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(intLenWord) + " letters long"
     
    while numGuesses > 0:
        
        print "-------------"
        availableLetters = getAvailableLetters(adivinadas)

        if isWordGuessed(secretWord, adivinadas):
            print "Congratulations, you won!"
            break

        print "You have " + str(numGuesses) + " guesses left."
        print "Available letters: " + availableLetters
        guess = raw_input("Please guess a letter: ")

        if len(guess) > 1:
            print "Please enter only one letter"
            continue
        guess = guess.lower()

        if guess not in availableLetters:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, adivinadas)

        elif guess in secretWord:
            adivinadas += guess
            print "Good Guess: " + getGuessedWord(secretWord, adivinadas)

        else:
            adivinadas += guess
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, adivinadas)
            numGuesses -= 1
 
    if numGuesses == 0:

        print "-------------"
        print "Sorry, you ran out of guesses. The word was " + secretWord


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
 
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)