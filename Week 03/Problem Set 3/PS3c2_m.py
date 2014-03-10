secretWord = 'apple' 
lettersGuessed = []

def getGuessedWord (secretWord, lettersGuessed):
#grader - start

	intCount = 0
	strGuess = ""

	for char in secretWord:

		if char in lettersGuessed:
			strGuess += char + " "
		else:
			strGuess += "_ "

	return strGuess

#grader - end
print getGuessedWord (secretWord, lettersGuessed)