def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L

    Counter = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            Counter += 1
            if L[j] < L[i]:
                Counter += 1
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                #print L
    print Counter
    #print "Final L: ", L

L = [7,6,5,4,3,2,1]
swapSort(L)