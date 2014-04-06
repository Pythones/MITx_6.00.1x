    # Create a new variable to store the maximum score seen so far (initially 0)
    score = 0
    max_score = 0 

    # Create a new variable to store the best word seen so far (initially None)
    best_word = "" 

    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word
    # return the best word you found.
    if best_word == "":
        return "None"
    else:
        return best_word