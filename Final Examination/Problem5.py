### Version 1
# def uniqueValues(aDict):
#     '''
#     aDict: a dictionary
#     returns: a sorted list of keys that map to unique aDict values, empty list if none
#     '''
#     # Your code here
#     returnlist = []
#     oncefreq = []
#     blacklist = []
#     bandlist = []

#     if aDict == {}:
#         return returnlist

#     for ele in aDict.items():
#         blacklist.append(ele[1])
#         # print(blacklist)
#         if ele[1] not in oncefreq and blacklist.count(ele[1]) == 1 and ele[1] != 0:
#             oncefreq.append(ele[1])
#         else:
#             bandlist.append(ele[1])

#     # print(oncefreq)

#     for ele in aDict.items():
#         if ele[1] in oncefreq and ele[1] not in bandlist:
#             returnlist.append(ele[0])
    
#     returnlist.sort()

#     return returnlist

### Version 2
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    keyList = []
    keyDict = {}

    for key in list(aDict.keys()):
        if aDict[key] not in keyDict:
            keyDict[aDict[key]] = 1

        else:
            keyDict[aDict[key]] += 1

    for keyInkeyDict in keyDict.keys():
        if keyDict[keyInkeyDict] == 1:
            for keyInaDict in aDict.keys():
                if aDict[keyInaDict] == keyInkeyDict:
                    keyList.append(keyInaDict)
    
    print(keyDict)
    
    return sorted(keyList)


print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))
    

    
