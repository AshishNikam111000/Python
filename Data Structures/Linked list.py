class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList():
    def __inti__(self):
        self.head = None
    
    def atend(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr:
            if itr.next == None:
                break
            itr = itr.next
        itr.next = Node(data, None)
        return
        
    def print(self):
        if self.head == None:
            print("Linked list is empty")
            return
        itr = self.head
        lst = ""
        while itr:
            lst += str(itr.data) + " --> "
            itr = itr.next
        print(lst)
        
    def insert_values(self, lst):
        self.head = None
        for i in lst:
            self.atend(i)
        
    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            print("Linked list is empty")
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
        
    def getindex(self, data):
        counter = 0
        flag = False
        if self.head == None:
            print("Linked List is empty")
            return
        itr = self.head
        while itr:
            if itr.data == data:
                flag = True
                break
            itr = itr.next
            counter += 1
        return counter, flag
    
    def remove_by_value(self, data):
        counter = 0
        index, status = self.getindex(data)
        if self.head == None:
            print("Linked List is empty")
            return
        if index==0:
            self.head = self.head.next
            return
        itr = self.head
        if status:
            while itr:
                if counter == index - 1:
                    itr.next = itr.next.next
                    break
                counter += 1
                itr = itr.next
        else:
            print("Element doesn't exsits")
            return
    
    
ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()

