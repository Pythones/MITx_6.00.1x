import string
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'l']

############################
#CODE TO PASTE
############################

def getAvailableLetters(lettersGuessed):

	strAvailableLetters = ''
	strAllLetters = string.ascii_lowercase

	for letter in strAllLetters:

		if letter not in lettersGuessed:

			strAvailableLetters += letter

	return strAvailableLetters


############################
#OUTPUT
############################

print getAvailableLetters(lettersGuessed)