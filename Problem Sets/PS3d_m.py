import string
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
#grader - start
	
	strAbc = string.ascii_lowercase
	strGuess = ""

	for char in strAbc:
		if char in lettersGuessed:
			strGuess += ""
		else:
			strGuess += char

	return strGuess


#grader - end
print getAvailableLetters(lettersGuessed)