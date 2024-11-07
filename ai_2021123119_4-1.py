class Node:
    pass

class CircularIterator:
    def __init__(self, h: Node):
        self.header = h
        self.prev = h
        self.cur = h.next

    def atEnd(self) -> bool:
        return self.cur is self.header

    def getData(self) -> int:
        if self.atEnd():
            return -1
        return self.cur.data

    def next(self):
        self.prev = self.cur
        self.cur = self.cur.next

    def insertAfter(self, x: int):
        newnode = Node()
        newnode.data = x
        newnode.next = self.cur.next
        self.cur.next = newnode


class Pioneer(CircularIterator):
    def atlasttown(self) -> bool:
        return self.cur.next is self.header
    
    def move(self):
        if not self.atlasttown():
            self.prev = self.cur
            self.cur = self.cur.next

    def build(self, x: int):
        newnode = Node()
        newnode.owner = x
        newnode.next = self.cur.next
        self.cur.next = newnode


class CircularLinkedList:
    def __init__(self):
        newnode = Node()
        newnode.next = newnode
        self.header = newnode

    def isEmpty(self) -> bool:
        return self.header.next is self.header

    def getIterator(self) -> Pioneer:
        return Pioneer(self.header)

Towns = CircularLinkedList()

k, n = input().split()
k = int(k)
n = int(n)

pioneers = []

list_for_n = []

for i in range(k):
    pioneer = Towns.getIterator()
    pioneers.append(pioneer)

for i in range(n):
    p , w = input().split()
    p = int(p)
    pioneer = pioneers[p]
    if w == "build" :
        pioneer.build(p)
    else :
        pioneer.move()
    


iterator = Towns.getIterator()
count = 0
while not iterator.atEnd():
    count += 1
    iterator.next()

print(count)


iterator = Towns.getIterator()
while not iterator.atEnd():
    print(iterator.cur.owner)
    iterator.next()