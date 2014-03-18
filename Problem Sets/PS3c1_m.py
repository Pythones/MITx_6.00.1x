secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord (secretWord, lettersGuessed):
#grader - start

	dblLenthA = len(secretWord)
	dblLenthB = len(lettersGuessed)
	intCount = 0
	strGuess = ""

	for i in range (dblLenthA):
		intCount = 0

		for j in range (dblLenthB):

			if secretWord [i] == lettersGuessed [j]:
				strGuess += str(secretWord [i]) + " "
				break
			else:
				intCount += 1
				if intCount == dblLenthB:
					strGuess += str("_ ")

	return strGuess

#grader - end
print getGuessedWord (secretWord, lettersGuessed)