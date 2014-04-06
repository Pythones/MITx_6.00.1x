hand = {'a': 2, 'b': 1}
filteredList = ["aba","lac","per","zzz"]


def AreAllLettersinHand(hand,filteredList):


    matchWord = []
    handLength = sum(hand.values()) #Longitud de la hand
    #print str(handLength) + " handLength"


    #buscamos si cada letra de la palabra esta en el dict de hand
    for word in filteredList:

        wordScore = 0
        charScore = 0

        for char in word:

            if hand.get(char, 0) != 0:
                charScore += 1
                hand[char] -= 1
                #print charScore

                wordScore += charScore
                #print str(wordScore) + " wordScore"

        if wordScore == handLength:
            matchWord.append(word)

    return matchWord

if __name__ == '__main__':
    print AreAllLettersinHand(hand,filteredList)
