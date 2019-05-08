import numpy as np
import random as rd


def predictor(data):
  data = data.split(",")
  caseList = np.array([data[0:3], data[3:6], data[6:9]])

  diagonal0 = [caseList[0][0], caseList[1][1], caseList[2][2]]
  diagonal1 = [caseList[0][2], caseList[1][1], caseList[2][0]]

  if len(set(diagonal0)) == 1 :
    if diagonal0[0] != 'b':
        return diagonal0[0]

  if len(set(diagonal1)) == 1:
    if(diagonal1[0] != 'b'):
        return diagonal1[0]

  for i in range(3):
    h = caseList[i, :]
    v = caseList[:, i]
    if len(set(h)) == 1:
      if h[0] != 'b':
        return h[0]

    elif len(set(v)) == 1 :
      if v[0] != 'b':
        return v[0]

  return "d"
def toString(data):
	s = ""
	for i in range(9):
		s=s+data[i]
		if i != 8:
			s = s +","
	return s

def testwin(data):
	s = toString(data)
	r = predictor(s)
	if r == "d" or r == "b":
		return False
	return True
		

test = "x,o,o,o,x,o,b,x,x,positive"
result = predictor(test)

if result == 'x':
  print("X won")

elif result == 'o':
  print("O won")

else:
  print("Draw")
def generator():
	ls =[0,1,2,3,4,5,6,7,8]
	b = 'b'
	lst = [b,b,b,b,b,b,b,b,b]
	for i in range(9):
		t = int(rd.choice(ls))
		if i %2 ==0:
			lst[t] = 'x'
		else:
			lst[t] = 'o'
		ls.remove(t)
		toString(lst)
		if(testwin(lst)):
			break
	#print(ls,lst)
	S = toString(lst)
	if predictor(toString(lst)) == 'x':
		S = S + ",positive"
	else:
		S = S + ",negative"
	return S
	
	
def visual(data):
	e = 0
	s = []
	for i in data:
		if i == 'x' or i == 'o' or i == 'b':
			s.append(i)
	
	data = s
	print(data[0], "|" ,data[1], "|", data[2])
	print(data[3], "|" ,data[4], "|", data[5])
	print(data[6], "|" ,data[7], "|", data[8])

pathwrite = r"C:\Users\carlg\Desktop\Machine Learning\experiment.txt"
filewrite = open(pathwrite,'w')
lst = []
for i in range(20000):
	g =(generator())
	if g not in lst:
		lst.append(g)
	print(g,len(lst))
	filewrite.write(g+"\n")
	visual(g)
	
	

	