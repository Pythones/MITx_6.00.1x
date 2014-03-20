hand = {'a': 2, 'b': 1}
filteredList = ["aba","loc","per","zzz"]
word = filteredList


def AreAllLettersinHand(hand,word):

    wordScore = 0
    matchWord = []
    handLength = sum(hand.values()) #Longitud de la hand

    #buscamos si cada letra de la palabra esta en el dict de hand
    for word in filteredList:

        for char in word:

            if hand.get (char, 0) == 1:  #si la hay suma uno
                wordScore += 1

        if wordScore == handLength:
            matchWord.append(word)

    return matchWord


if __name__ == '__main__':
    print AreAllLettersinHand(hand,word)