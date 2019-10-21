class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next


# linkedlist with 3 nodes


linkl = Node(1)
linkl.head = LinkedList()

second = Node(2)
third = Node(3)

linkl.next = second
second.next = third