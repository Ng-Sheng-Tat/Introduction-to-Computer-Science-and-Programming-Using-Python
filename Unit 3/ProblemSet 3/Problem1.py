def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    bol = False
    mylist = []
    for alphabet in secretWord:
        if alphabet in lettersGuessed:
            mylist.append(1)
        else:
            mylist.append(0)
    
    if 0 not in mylist:
        bol = True
    
    return bol