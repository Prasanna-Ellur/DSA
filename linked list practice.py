class Node:
    def __init__(self,item,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start):
        self.start=start
    def is_empty(self):
        self.start=None
    def insert_at_first(self,data):
        n=Node(data)

        self.start=n
    def insert_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def find_middle(self):
        slow=self.start
        fast=self.start
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        if slow is not None:
            return slow.item
        else:
            return None
        
mylist = SLL()
mylist.insert_last(10)
mylist.insert_last(20)
mylist.insert_last(30)
mylist.insert_last(40)
mylist.insert_last(50)

print("Middle element:", mylist.find_middle())
