import random as rd


class node:
    childX = None
    childO = None
    childB = None
    parent = None
    symbol = None

    def __init__(self, value):
        self.value = value

    def addChild(self, child, symbol):
        if symbol == x:
            self.childX = child
        elif symbol == o:
            self.childO = child
        else:
            self.childB = child
        child.parent = self
        child.symbol = symbol

    def getChildList(self):
        return [[x, self.childX], [o, self.childO], [b, self.childB]]


def printTree(root):
    for i in root.getChildList():

        if i[1] != None:
            print(root.value, end=" ")
            print("---", i[0], "--->", i[1].value, end=" ")
            printTree(i[1])
            print()


x = 'x'
o = 'o'
b = 'b'

root = node(3)
t = node(6)
print(t.value)

root.addChild(t, x)
print(t.parent.value, t.symbol)
printTree(root)

lst = []
for i in range(0, 23):
    r = rd.randint(0, 100)

    lst.append(node(r))

d = [x, o, b]

