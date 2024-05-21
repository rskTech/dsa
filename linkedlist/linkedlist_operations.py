class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtBegin(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
    def insertAtEnd(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            if cur_node != None:
                cur_node.next = node
    def display(self):
        if self.head == None:
            print("LinkedList is empty")
        else:
            cur_node = self.head
            while cur_node != None:
                print(cur_node.data, end='->')
                cur_node = cur_node.next
ll = LinkedList()
ll.insertAtBegin(1)
ll.insertAtBegin(2)
ll.insertAtBegin(3)
ll.insertAtEnd(4)
ll.display()
