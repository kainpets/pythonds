def ListElementFinderOne(theList):
    minimum = 0
    for i in range(len(theList)):
        if (theList[i] < minimum):
            minimum = theList[i]           
    return minimum


def ListElementFinderTwo(theList):
    return min(theList)


myList = [0,1,2,3,4,5]
print(ListElementFinderOne(myList))
print(ListElementFinderTwo(myList))
