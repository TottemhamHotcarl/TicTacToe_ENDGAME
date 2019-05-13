from sqlite3 import Cache

from prettytable import PrettyTable
import math
import queue
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import graphviz

class node:
	childX = None
	childO = None
	childB = None
	parent = None
	symbol = None
	data = None
	whiteList = None
	outcome = None

	def __init__(self, value):
		self.value = value


	def addChild(self, child, symbol,white):
		if symbol == 'x':
			self.childX = child
		elif symbol == 'o':
			self.childO = child
		else:
			self.childB = child
		child.parent = self
		child.symbol = symbol
		t = self.whiteList.copy()
		t.remove(white)
		child.whiteList = t

	def getChildList(self):
		return [['x', self.childX], ['o', self.childO], ['b', self.childB]]


def printTree(root):
	if(root.value != None):
		print(root.value)
		for i in root.getChildList():

			if i[1] != None:
				print(root.value, end=" ")
				print("---", i[0], "--->", i[1].value, end=" ")
				printTree(i[1])
			print()






def nicePrint(Title, data):	#printing pretty table of data
	x = PrettyTable()
	x.field_names = Title
	for i in range(len(data)):
		x.add_row(data[i])
	print(x)


def getData():	#receiving data from file and arranging the data within a list form
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


def getTestData():
    path = r"C:\Users\carlg\Desktop\Machine Learning\test-validating.txt"

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






def Entropy(probability):	#simple function to work out entropy that takes in the parameters of probability
	entropy = 0
	for i in probability:	#probability is a list with probOfPositive and negative
		if i != 0:
			entropy = entropy + float(i)*math.log2(float(i))

	return (entropy * -1)


def calculateMainEntropy(data):	#function to work out entropy
	if (len(data)) != 0:
		class_index = len(data[0])-1	#refer to last column that contains 1 or 0
		numberOfPositive = 0
		numberOfNegative= 0
		total = 0

		for i in range(len(data)):		#iterate through every row in data
			if data[i][class_index] == 1:
				numberOfPositive = numberOfPositive + 1		#if there is a 1, update the number of occurances
			elif data[i][class_index] == 0:
				numberOfNegative = numberOfNegative + 1		#if there is a 0, update the number of occurances

			total += 1

		probOfPositive = numberOfPositive/total		#prob of 1's occuring
		probOfNegative = numberOfNegative/total		#prob of 0's occuring

		p = [probOfPositive, probOfNegative]		#list of probOfPositive and negative
		return Entropy(p)
	return 0


def partitionDataX(data, n):		#search through given column and create a new array which contains all the x's from that column
	x_data = []
	attribute_value = []
	for i in range (len(data)):
		if data[i][n] == "x":
			x_data.append(data[i])
	return x_data

def partitionDataO(data, n):		#search through given column and create a new array which contains all the o's from that column
	o_data = []
	attribute_value = []
	for i in range (len(data)):
		if training_data[i][n] == "o":
			o_data.append(data[i])
	return o_data

def partitionDataB(data, n):		#search through given column and create a new array which contains all the b's from that column
	b_data = []
	attribute_value = []
	for i in range (len(data)):
		if data[i][n] == "b":
			b_data.append(data[i])
	return b_data


def gain(data, n):		#given data and specific column, work out the gain from each column given

	dataX = partitionDataX(data, n)		#create new array of all x's in specific column
	dataO = partitionDataO(data, n)		#create new array of all o's in same column
	dataB = partitionDataB(data, n)		#create new array of all b's in same column

	main_entropy = calculateMainEntropy(data)	#entropy of the whole data set
	x_entropy = calculateMainEntropy(dataX)		#entropy of the x's in specific column
	o_entropy = calculateMainEntropy(dataO)		#entropy of the x's in same column
	b_entropy = calculateMainEntropy(dataB)		#entropy of the x's in same column

	length_whole = len(data)	#total number of rows in data set
	length_x = len(dataX)		#total number of x's in column
	length_o = len(dataO)		#total number of o's in column
	length_b = len(dataB)		#total number of b's in column

	sum = (length_x * x_entropy) + (length_o * o_entropy) + (length_b * b_entropy)
	#print("sum", sum)
	if sum != 0:
		gain = main_entropy - (1/length_whole * (sum))

		return gain
	return 0


def findBestGain(data, whitelist4):		#iterate through every column and calculate the gain
	numOfCol = 9
	array = []
	for i in range(numOfCol):
		if i in whitelist4:
			array.append(gain(data, i))		#append gain of each column to an array to find max value
		else:
			array.append(-10000000)
	if(max(array)!= -10000000):
		return [max(array), array.index(max(array))]
	return [max(array), -1]


Title = ["top-left", "top-middle",  "top-right", "middle-left", "middle-middle", "middle-right",  "bottom-left", "bottom-middle", "bottom-right", "outcome"]

nicePrint(Title, getData())
training_data = getData()
partitioned_data1 = partitionDataX(training_data, 0)
partitioned_data2 = partitionDataO(training_data, 0)
partitioned_data3 = partitionDataB(training_data, 0)

#print(training_data)

print("")
print("Main Entropy: " + str(calculateMainEntropy(training_data)))
print("x entropy: " + str(calculateMainEntropy(partitioned_data1)))
print("o entropy: " + str(calculateMainEntropy(partitioned_data2)))
print("blank entropy: " + str(calculateMainEntropy(partitioned_data3)))
print("")



blacklist = []


def getMostlyResult(data):
    pos = 0
    neg = 0


    for i in data:

        if i[9] == 1:
            pos = pos + 1
        else:
            neg = neg + 1

    if pos >= neg:
        return " positive"
    else:
        return " negative"


def myTreeToAnyTree(parent):
    pNode = Node(str(parent.value), display_name = " " + str(parent.value))
    ptemp = pNode
    LNode= queue.Queue(maxsize=100)
    LmyNode= queue.Queue(maxsize=100)
    LNode.put(pNode)
    LmyNode.put(parent)
    q = 2300
    lst.append(pNode)

    while LmyNode.qsize() != 0:
        tn = LmyNode.get()
        ptemp = LNode.get()





        if tn.childX is not None:
            tx = Node(str(q) + "x" + str(tn.childX.value), parent = ptemp, display_name=  "x" + str(tn.childX.value))
            LNode.put(tx)
            LmyNode.put(tn.childX)
            q = q +1
            lst.append(tx)
        else:
            tr = partitionDataX(tn.data,tn.value)
            out = getMostlyResult(tr)
            w = Node(str(q) + str(out), parent=ptemp, display_name=  "x" + str(out))
            q = q + 1
        if tn.childO is not None:
            to = Node(str(q) + "o" + str(tn.childO.value), parent = ptemp  , display_name= "o" + str(tn.childO.value))
            LNode.put(to)
            LmyNode.put(tn.childO)
            q = q + 1
            lst.append(to)
        else:
            tr = partitionDataO(tn.data,tn.value)
            out = getMostlyResult(tr)
            w = Node(str(q) + str(out), parent=ptemp, display_name=  "o" + str(out))
            q = q + 1
        if tn.childB is not None:
            tb = Node(str(q) + "b" + str(tn.childB.value), parent = ptemp,  display_name= "b" + str(tn.childB.value))
            LNode.put(tb)
            LmyNode.put(tn.childB)
            q = q + 1
            lst.append(tb)
        else:
            tr = partitionDataB(tn.data,tn.value)
            out = getMostlyResult(tr)
            w = Node(str(q) + str(out), parent=ptemp, display_name=  "b" + str(out))
            q = q + 1

    return pNode







def getChildern(root):
    store = [-1, -1, -1]
    root.outcome = getMostlyResult(root.data)

    # childX
    DataX = partitionDataX(root.data, root.value)
    DataO = partitionDataO(root.data, root.value)
    DataB = partitionDataB(root.data, root.value)
    if len(DataX) != 0 and root.whiteList is not None:

        print(root.whiteList)
        temp = findBestGain(DataX, root.whiteList)
        if temp[1] != -1:
            root.addChild(node(temp[1]), 'x', temp[1])
            root.childX.data = DataX
            store[0] = temp[1]
            root.whiteList.remove(temp[1])
            root.childX.outcome = getMostlyResult(root.childX.data)

    # childO

    if len(DataO) != 0 and root.whiteList is not None:
        # nicePrint(Title, DataO)
        # nicePrint(Title, DataX)
        temp = findBestGain(DataO, root.whiteList)
        if temp[1] != -1:
            root.addChild(node(temp[1]), 'o', temp[1])
            root.childO.data = DataO
            store[1] = temp[1]
            root.whiteList.remove(temp[1])
            root.childO.outcome = getMostlyResult(root.childO.data)




    # childB

    if len(DataB) != 0  and root.whiteList != None:
        #nicePrint(Title, DataB)
        # nicePrint(Title, DataX)
        temp = findBestGain(DataB, root.whiteList)
        if temp[1] != -1:
            root.addChild(node(temp[1]), 'b', temp[1])
            root.childB.data = DataB
            store[2] = temp[1]
            root.whiteList.remove(temp[1])
            root.childB.outcome = getMostlyResult(root.childB.data)

    return [root, store]


print("ENDGAME ?>?>?>?>?>?>?>??>?>?>?>?>?>?>?>?>?>?>?")

#temp = findBestGain(training_data,[0,1,2,3,4,5,6,7,8])
#root23 = node(temp[1])
#root23.data = training_data
#root23.whiteList = [0,1,2,3,4,5,6,7,8]
#root23.whiteList.remove(temp[1])
#parent = root23
#parentS = parent

parent = node(4)
parent.data = training_data
parent.whiteList = [0,1,2,3,5,6,7,8]



L = queue.Queue(maxsize=100)

L.put(parent)

while L.qsize() != 0:
    print("size = ", L.qsize())
    curr = L.get()
    print("inital whiteList = ", curr.whiteList)
    t = getChildern(curr)
    rootTemp = t[0]
    print(rootTemp.whiteList)
    if rootTemp.whiteList == []:
        continue
    R = t[1]
    if R[0] != -1:
        L.put(rootTemp.childX)
    if R[1] != -1:
        L.put(rootTemp.childO)
    if R[2] != -1:
        L.put(rootTemp.childB)
    print("final whiteList = ", curr.whiteList)





lst =[]






#printTree(parent)


for pre, fill, node in RenderTree(myTreeToAnyTree(parent)):
	print("%s%s" % (pre, node.name))

t = myTreeToAnyTree(parent)

DotExporter(t).to_dotfile('udo.dot')

DotExporter(lst[0],
            nodeattrfunc=lambda node: 'label="{}"'.format(node.display_name[1::]),
			edgeattrfunc=lambda edge,node: 'label="{}"'.format(node.display_name[0])).to_dotfile("graph.txt")







def runID3(parent, test):
    parentTemp = parent
    while True:
        v = parentTemp.value
        tem = test[v]


        if tem == 'x':
            if parentTemp.childX is not None:
                parentTemp = parentTemp.childX
            else:
                return parentTemp.outcome
        elif tem == 'o':
            if parentTemp.childO is not None:
                parentTemp = parentTemp.childO
            else:
                nicePrint(Title,parentTemp.data)
                return parentTemp.outcome

        elif tem == 'b':
            if parentTemp.childB is not None:
                parentTemp = parentTemp.childB
            else:
                return parentTemp.outcome




TestList = getTestData()
#nicePrint(Title,TestList)

ConfusionMatrix = []
ConfusionMatrix.append([0,0])
ConfusionMatrix.append([0,0])

for i in TestList:
    guess = runID3(parent,i)
    if guess == " positive":
        guessValue = 1
    else:
        guessValue = 0
    actualValue = i[9]

    ConfusionMatrix[guessValue][actualValue] = ConfusionMatrix[guessValue][actualValue] + 1

print(ConfusionMatrix)
diagonal = ConfusionMatrix[0][0] + ConfusionMatrix[1][1]
total = ConfusionMatrix[0][0] + ConfusionMatrix[0][1] + ConfusionMatrix[1][0] + ConfusionMatrix[1][1]
print(diagonal/total*100, "%")





nicePrint(Title, parent.childB.childO.data)
