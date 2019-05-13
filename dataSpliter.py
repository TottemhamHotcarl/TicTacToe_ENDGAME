import random

path = r"C:\Users\carlg\Desktop\Machine Learning\Fulldata.txt"

file_object  = open(path, 'r')

i = 0
lst = []
n = 958*(0.0) #%of testing data
while i < n:
	r = random.randint(0,957)
	if r not in lst:
		lst.append(r)
		i = i + 1

pathwrite = r"C:\Users\carlg\Desktop\Machine Learning\test-validating.txt"
filewrite = open(pathwrite,'w')
pathwrite2 = r"C:\Users\carlg\Desktop\Machine Learning\training1.txt"
filewrite2 = open(pathwrite2,'w')


i = 0
b = file_object.readline()
lists = []
while b != "":
	print(b)
	temp = b.split(",")
	lists.append(b)
	b = file_object.readline()
tr =[]
for i in range(958):
	if i not in lst:
		tr.append(i)
for i in lst:
	filewrite.write(lists[i])
random.shuffle(tr)

for i in tr:
	filewrite2.write(lists[i])
	



	
