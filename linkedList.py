class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insertAtEnd(self, newNode):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def insertAtStart(self, newNode):
        current = self.head
        if current:
            current = newNode
            current.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def delete(self, value):
        current = self.head
        if current.data == value:
            self.head = current.next
        else:
            while current:
                if current.data == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

    def search(self, value):
        current = self.head
        if not current:
            raise IndexError("This Linked List is empty.")
        count = 0
        if current.data == value:
            print(f"Value {value} found at index {count}")
        else:
            while current:
                if current.data == value:
                    break
                current = current.next
                count += 1
            if current:
                print(f"Value {value} found at index {count}")
            else:
                print(f"Value {value} not found")

    def pop(self):
        current = self.head
        if not current:
            raise IndexError("This Linked List is empty.")
        else:
            while current:
                if not current.next:
                    break
                prev = current
                current = current.next
            prev.next = None
            current.data = None
        

    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

testNode = Node(1)
testNode2 = Node(2)
testNode3 = Node(3)
testNode4 = Node(4)
testNode5 = Node(5)
testNode6 = Node(6)

testList = LinkedList()
testList.insertAtStart(testNode)
testList.insertAtEnd(testNode2)
testList.insertAtStart(testNode3)
testList.insertAtEnd(testNode4)
testList.insertAtStart(testNode5)
testList.insertAtStart(testNode6)
testList.print()
print("\n Now testing pop and search:")
testList.pop()
testList.pop()

testList.print()
testList.search(6)
testList.search(5)
testList.search(2)
testList.search(4)