from prettytable import PrettyTable
import numpy as np
def nicePrint(Title, data):
    x = PrettyTable()
    x.field_names = Title
    for i in range(len(data)):
        x.add_row(data[i])
    print(x)



def getData():
    path = r"C:\Users\carlg\Desktop\Machine Learning\training1.txt"

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
print(Data)
Title = ["TL","TM","TR","ML","MM","MR","BL","BM","BR","OUTCOME"]
nicePrint(Title,Data)

positiveTable = []
positiveTableTitle = ["Square", "X", "O", "b"]
neqativeTable = []
negativeTableTitle = ["Square", "X", "O", "b"]

for i in range(9):
    t = propabilityCol(Data,i,1)
    positiveTable.append([i, t[0], t[1] ,t[2]])
    t = propabilityCol(Data, i, 0)
    neqativeTable.append([i, t[0], t[1], t[2]])

print("Positive")
nicePrint(positiveTableTitle,positiveTable)
print()
print("Negative")
nicePrint(negativeTableTitle,neqativeTable )


test = "o,b,x,o,x,x,o,b,b"

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
testarr = cleanTestInput(test)
prod = 1
