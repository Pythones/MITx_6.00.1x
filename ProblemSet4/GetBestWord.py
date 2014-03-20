#Take a list of words and return the one with higher value.

def GetBestWord(wordList,n):
	higherScore = 0
	bestWord = ''
	for word in wordList:
		wordScore = getWordScore(word, n)
		if wordScore > higherScore:
			higherScore = wordScore
			bestWord = word

	return word