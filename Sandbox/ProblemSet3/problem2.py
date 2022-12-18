def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    tobereturn = ['_' for i in range(len(secretWord))]
    # print(tobereturn)
    
    for let in lettersGuessed:
        for i in range(len(secretWord)):
            if secretWord[i] == let:
                tobereturn[i] = let
    
    # print(tobereturn)
    emptystr = ''
    for ele in tobereturn:
      emptystr += ele
    return emptystr
