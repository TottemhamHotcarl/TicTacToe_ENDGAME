from prettytable import PrettyTable
import numpy as np
def nicePrint(Title, data):
    x = PrettyTable()
    x.field_names = Title
    for i in range(len(data)):
        x.add_row(data[i])
    print(x)



def getData():
    path = r"C:\Users\carlg\Desktop\Machine Learning\experiment.txt"

    file_object = open(path, 'r')

    i = 0
    b = file_object.readline()
    lists = []
    while b != "":
        temp = b.split(",")
        r = []
        for i in range(10):
            if i != 9:
                r.append(str(temp[i]).strip())
            elif i == 9:
                if temp[i] == "negative\n":
                    r.append(0)
                elif temp[i] == "positive\n":
                    r.append(1)
        lists.append(r)
        b = file_object.readline()
    return lists

def getTestData():
    path = r"C:\Users\carlg\Desktop\Machine Learning\Fulldata.txt"

    file_object = open(path, 'r')

    i = 0
    b = file_object.readline()
    lists = []
    while b != "":
        temp = b.split(",")
        r = []
        for i in range(10):
            if i != 9:
                r.append(str(temp[i]).strip())
            elif i == 9:
                if temp[i] == "negative\n":
                    r.append(0)
                elif temp[i] == "positive\n":
                    r.append(1)
        lists.append(r)
        b = file_object.readline()
    return lists


def propabilityCol(data, col,outcome):
    numX = 0
    numO = 0
    numb = 0
    numTotal = 0

    for i in data:
        if i[col] == 'x' and i[9] == outcome:
            numX = numX + 1
            numTotal = numTotal + 1
        elif i[col] == 'o' and i[9] == outcome:
            numO = numO + 1
            numTotal = numTotal + 1
        elif i[col] == 'b' and i[9] == outcome:
            numb = numb + 1
            numTotal = numTotal + 1
    return [numX/numTotal,numO/numTotal,numb/numTotal]

Data = getData()
Title = ["TL","TM","TR","ML","MM","MR","BL","BM","BR","OUTCOME"]
nicePrint(Title,Data)



def getProbabilities(Data):

    numPos = 0
    numNeg = 0
    total = 0
    for i in Data:
        if i[9] == 1:
            numPos = numPos + 1
            total = total + 1
        elif i[9] == 0:
            numNeg = numNeg + 1
            total = total + 1
    return [numPos/total, numNeg/total]





positiveTable = []
positiveTableTitle = ["Square", "X", "O", "b"]
negativeTable = []
negativeTableTitle = ["Square", "X", "O", "b"]

for i in range(9):
    t = propabilityCol(Data,i,1)
    positiveTable.append([i, t[0], t[1] ,t[2]])
    t = propabilityCol(Data, i, 0)
    negativeTable.append([i, t[0], t[1], t[2]])

print("Positive")
nicePrint(positiveTableTitle,positiveTable)
print()
print("Negative")
nicePrint(negativeTableTitle,negativeTable )




def cleanTestInput(t):
    temp = t.split(",")
    arr = []
    for i in temp:
        arr.append(i)
    print(arr)
    return arr

def getIndex(c):
    if c == "x":
        return 1
    elif c == 'o':
        return 2
    else:
        return 3

#postive

test = "o,x,o,x,b,o,x,x,o"
def naivebayesPositiveCalc(positiveTable,test):
    Pp = 1
    i = 0
    while i<9:
        t = getIndex(test[i])
        Pp = Pp*positiveTable[i][t]
        i = i+1
    return Pp
def naivebayesNegativeCalc(negativeTable,test):
    Pn = 1
    i = 0
    while i<9:
        t = getIndex(test[i])
        Pn = Pn*negativeTable[i][t]
        i = i+1
    return Pn


def zlatan(test):
    Pxgivenpos = naivebayesPositiveCalc(positiveTable,test)
    Pxgivenneg = naivebayesNegativeCalc(negativeTable, test)
    temp = (getProbabilities(Data))
    Ppos = temp[0]
    Pneg = temp[1]


    dem = Pxgivenneg*Pneg + Pxgivenpos*Ppos
    p = Pxgivenpos*Ppos/dem
    n = Pxgivenneg*Pneg/dem
    #print("Probability of winning: ", Pxgivenpos*Ppos/dem)
    #print("Probability of lossing: ", Pxgivenneg*Pneg/dem)
    if p >= n:
        return 1
    else:
        return 0

print(zlatan(test))
print("pizza")
testDate = getTestData()
lst = []
for i in testDate:
    temp =[]
    t = ""
    for j in range(9):
        t = t + i[j]
    temp.append(t)
    temp.append(i[9])
    lst.append(temp)

ConfusionMatrix = []
ConfusionMatrix.append([0,0])
ConfusionMatrix.append([0,0])


for i in lst:
    guess = zlatan(i[0])
    actualValue = i[1]

    ConfusionMatrix[actualValue][guess] = ConfusionMatrix[actualValue][guess] + 1
print(ConfusionMatrix)
diagonal = ConfusionMatrix[0][0] + ConfusionMatrix[1][1]
total = ConfusionMatrix[0][0] + ConfusionMatrix[0][1] + ConfusionMatrix[1][0] + ConfusionMatrix[1][1]
print(diagonal/total*100, "%")