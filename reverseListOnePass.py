# !usr/bin/env python

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def addNode(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def printList(self):
        temp = self.head
        while temp.next != None:
            print temp.data,
            print '->',
            temp = temp.next
        if temp.next == None :
            print temp.data


    def reverseList(self):
        if self.head == None:
            print "No list present"
        if self.head.next == None:
            return
        temp1 = self.head
        temp2 = self.head.next
        temp3 = temp2.next
        temp1.next = None

        if temp2.next == None:
            temp2.next = temp1
            temp1.next = None
            self.head = temp2
            return
        if temp3.next == None:
            temp3.next = temp2
            temp2.next = temp1
            self.head = temp3
            temp1.next = None
            return
        while(temp3.next != None):
            self.head = temp3
            nextleap = temp3.next
            temp3.next = temp2
            temp2.next = temp1
            temp1 = temp3
            temp2 = nextleap
            temp3 = temp2.next
            if temp3 == None :
                temp2.next = temp1
                self.head = temp2
                break
            if temp3.next == None:
                temp2.next= temp1
                temp3.next = temp2
                self.head = temp3
                break



llist = LinkedList()
llist.addNode(1)
llist.addNode(2)
llist.addNode(3)
llist.addNode(4)
llist.addNode(5)
llist.addNode(6)
llist.addNode(7)
llist.addNode(8)
llist.addNode(9)
llist.addNode(10)
llist.addNode(11)
llist.addNode(12)

llist.printList()
llist.reverseList()
llist.printList()
