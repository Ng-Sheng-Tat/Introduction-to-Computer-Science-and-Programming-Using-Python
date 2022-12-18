def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    completealp = string.ascii_lowercase
    emplist = []
    for i in completealp:
      emplist.append(i)
    # print(emplist)
    for item in lettersGuessed:
        # print(item)
        for alp in emplist:
          # print(alp)
          if item == alp:
            emplist.remove(item)
    tobereturn = ''
    for j in emplist:
      tobereturn += j
    # print(tobereturn)
    return tobereturn