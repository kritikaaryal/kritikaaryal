for a in [False,True]:
    for b in [False,True]:
        for c in [False,True]:
                print(a,b,c, (not a and b) or (c and not b) )