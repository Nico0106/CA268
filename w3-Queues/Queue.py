from Stack import Stack

class Queue:
    def __init__(self):
        self.es = Stack()
        self.ds = Stack()
        self.size = 0

    def isempty(self):
        return self.es.isempty() and self.ds.isempty()

    def enqueue(self, i):
        self.size += 1
        self.es.push(i)

    def dequeue(self):
        self.size -= 1
        if not self.dsk.isempty():
            return self.ds.pop()
        while not self.es.isempty():
            self.ds.push(self.es.pop())

        return self.ds.pop()
