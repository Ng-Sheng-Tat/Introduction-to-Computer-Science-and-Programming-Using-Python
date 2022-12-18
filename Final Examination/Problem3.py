def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    count = 1
    breakpoint = 0
    while k > breakpoint:
        k = k - count
        count = count + 1
        # print(k)
    if k == breakpoint:
        return True
    else:
        return False

print(is_triangular(21))