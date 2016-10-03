def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
     # Create a new variable to store the maximum score seen so far 
    # (initially 0)
    max_score = 0

    # Create a new variable to store the best word seen so far (initially None)
    best_word = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to 
        # test if the word is in the wordList - you can make a similar 
        # function that omits that test)
        if canConstruct(word, hand):

            # Find out how much making that word is worth
            word_score = getWordScore(word, n)

            # If the score for that word is higher than your best score
            if word_score > max_score:

                # Update your best score, and best word accordingly
                max_score = word_score
                best_word = word

    # return the best word you found.
    return best_word

def canConstruct(word, hand):
    letters = getFrequencyDict(word)

    for c in letters:
        if letters[c] > hand.get(c, 0):
            return False

    return True
