from collections import Counter

hand = {'a':2, 'b':1}
filteredList = word = ["aba", "abb", "abz"] 


def AreLettersInHand(hand,filteredList):
	for word in filteredList:
		count = Counter(word)
		
		print count


AreLettersInHand(hand,word)

print hand['a']