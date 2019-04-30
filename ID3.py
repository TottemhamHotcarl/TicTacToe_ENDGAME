from prettytable import PrettyTable
import math


class node:
    childX = None
    childO = None
    childB = None
    parent = None
    symbol = None
    data = None

    def __init__(self, value):
        self.value = value

    def addChild(self, child, symbol):
        if symbol == 'x':
            self.childX = child
        elif symbol == 'o':
            self.childO = child
        else:
            self.childB = child
        child.parent = self
        child.symbol = symbol

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
	print("sum", sum)
	if sum != 0:
		gain = main_entropy - (1/length_whole * (sum))

		return gain
	return 0


def findBestGain(data, blacklist):		#iterate through every column and calculate the gain
	numOfCol = 9
	array = []
	for i in range(numOfCol):
		if i not in blacklist:
			array.append(gain(data, i))		#append gain of each column to an array to find max value
		else:
			array.append(-10000000)
	return [max(array), array.index(max(array))]


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




def getChildern(root):
	#blacklist = [root.value]
	training_data = root.data
	DataX = partitionDataX(training_data, root.value)
	nicePrint(Title,DataX)
	# nicePrint(Title, DataX)
	temp = findBestGain(DataX, blacklist)
	root.addChild(node(temp[1]), 'x')
	root.childX.data = partitionDataX(root.data, temp[1])
	print("***********************************************************************************************************")
	nicePrint(Title, root.childX.data)
	# root = root.childX
	blacklist.append(temp[1])

	DataO = partitionDataO(training_data, root.value)
	# nicePrint(Title, DataO)
	temp = findBestGain(DataO, blacklist)
	root.addChild(node(temp[1]), 'o')
	# root = root.childO
	blacklist.append(temp[1])
	root.childO.data = partitionDataO(root.data, temp[1])
	DataB = partitionDataB(training_data, root.value)
	# nicePrint(Title, DataB)
	temp = findBestGain(DataB, blacklist)
	root.addChild(node(temp[1]), 'b')
	# root = root.childB
	blacklist.append(temp[1])
	root.childB.data = partitionDataB(root.data, temp[1])
	return root


temp = findBestGain(training_data,blacklist)
print(temp)
root = node(temp[1])
root.data = training_data

choice = ['x', 'o','b']


root2 = getChildern(root)
root3 = root2.childX

getChildern(root2.childX)

getChildern(root2.childO)
getChildern(root2.childB)
printTree(root2)

