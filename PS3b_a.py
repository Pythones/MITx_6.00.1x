secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'l']

############################
#CODE TO PASTE
############################

def isWordGuessed(secretWord, lettersGuessed):
	counter = 0
	for letter in secretWord:

		if letter in lettersGuessed:
			counter += 1

	if counter == len(secretWord):
		return True
	else:
		return False

############################
#OUTPUT
############################
print isWordGuessed(secretWord,lettersGuessed)