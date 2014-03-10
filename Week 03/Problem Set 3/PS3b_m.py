secretWord = 'carrot' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed = ['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't']

def isWordGuessed(secretWord, lettersGuessed):
#grader - start

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

#grader - end
print isWordGuessed (secretWord, lettersGuessed)