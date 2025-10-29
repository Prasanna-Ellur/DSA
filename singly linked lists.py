class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)
node1.next=node2
node2.next=node3
node3.next=node4
new_node=node(35)
head=node1
current=head
while current.data!=30:
    current=current.next
new_node.next=current.next
current.next=new_node
current=node1
while current is not None:
    print(current.data,end="--")
    current=current.next
print("None")

