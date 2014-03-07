secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'l']

############################
#CODE TO PASTE
############################

def getGuessedWord(secretWord, lettersGuessed):

	counter = 0
	strDisplayWord = ''

	for letter in secretWord:

		if letter in lettersGuessed:

			strDisplayWord += letter
		else:
			strDisplayWord += '_ '

	return strDisplayWord

############################
#OUTPUT
############################

print getGuessedWord(secretWord,lettersGuessed)