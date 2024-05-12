#write functions here, don't add input('') statements here!
def test_config():
    return True
def testHigh(listA):
    listA.sort()
    return listA[-1]
def testLow(listA):
    listA.sort()
    return listA[0]
def Total(listA):
    i=0
    totality = 0
    while i != 5:
        totality += listA[i]
        i+=1
    return totality
def Average(listA):
    i=0
    totality = 0
    while i != 5:
        totality += listA[i]
        i+=1
    return (totality/5)
