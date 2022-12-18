def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if word == '' or word not in wordList:
        return False

    handcopy = hand.copy()
    
    for wd in word:
        handcopy[wd] = handcopy.get(wd, 0) - 1
    
    for value in handcopy.values():
        if value < 0:
            return False
    
    return True
print(isValidWord('rapture', {'r': 1, 'u': 1, 'e': 1, 't': 1, 'p': 2, 'a': 3}, ['rapture', 'abc']))