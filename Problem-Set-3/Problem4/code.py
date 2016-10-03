def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = ""
    for c in string.ascii_lowercase:
        if c not in lettersGuessed:
            available += c

    return available
