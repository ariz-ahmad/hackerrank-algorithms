def compareTriplets(a, b):
    m, n = 0, 0
    for i, j in zip(a,b):
        if(i > j):
            m = m + 1
        elif(i < j):
            n = n + 1
    return [m, n]
