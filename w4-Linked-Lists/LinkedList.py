class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def ass(self, item):
        self.head = Node(item, self.head)

    def is_empty(self):
        return self.head == None

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            return item

    def display(ll):
        while not ll.is_empty():
            print(ll.remove())

def main():
