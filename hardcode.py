import numpy as np
def getData():
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

def test(x):
    t = predictor(x)
    if t == 'x':
        return "positive\n"
    return "negative\n"


ConfusionMatrix = []
ConfusionMatrix.append([0,0])
ConfusionMatrix.append([0,0])


def visual(data):
    e = 0
    s = []
    for i in data:
        if i == 'x' or i == 'o' or i == 'b':
            s.append(i)

    data = s
    print(data[0], "|", data[1], "|", data[2])
    print(data[3], "|", data[4], "|", data[5])
    print(data[6], "|", data[7], "|", data[8])


path = r"C:\Users\carlg\Desktop\Machine Learning\Fulldata.txt"

file_object  = open(path, 'r')


b = file_object.readline()

while b != "":
    t = b.split(",")
    guess = test(b)
    actual = t[9]

    visual(t)
    print(guess,actual)


    b = file_object.readline()



