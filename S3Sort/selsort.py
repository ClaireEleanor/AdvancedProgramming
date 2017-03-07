from random import randint as rand

def listGen(n):
    randlist = []
    for i in range(n):
        randlist.append(rand(1,100))
    return randlist

def findSmallest(sortlist):
    smallest = sortlist[0]
    smallest_index = 0
    for i in range(1, len(sortlist)):
        if sortlist[i] < smallest:
            smallest = sortlist[i]
            smallest_index = i
    return smallest_index

def selectionSort(sortlist):
    newsortlist = []
    for i in range(len(sortlist)):
        smallest = findSmallest(sortlist)
        newsortlist.append(sortlist.pop(smallest))
    return newsortlist


newlist = listGen(10)
print newlist
print selectionSort(newlist)
