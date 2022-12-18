def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    uniquelist = []
    freqdict = {}
    for ele in L:
        if ele not in uniquelist:
            uniquelist.append(ele)
    # print(uniquelist)

    for ele in uniquelist:
        freqdict[ele] = 0

    for ele in L:
        freqdict[ele] += 1
    # print(freqdict)

    maxval = 0
    for ele in freqdict.items():
        # print(ele[0], ele[1])
        if ele[0] > maxval and ele[1] % 2 == 1:
            maxval = ele[0]
            # print(ele[1])
            maxreturn = ele[0]
        #     print(maxreturn)
    # print(maxreturn)
    if maxval != 0:
        return maxreturn
    else:
        return None

print(largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2]))