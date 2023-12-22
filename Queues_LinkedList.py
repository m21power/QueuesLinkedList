class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
class Queues:
    def __init__(self):
        self.head=None
    def enque(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head =new_node
            return 
        iter=self.head
        while iter.next:
            iter=iter.next
        iter.next=new_node
    def deque(self):
        self.head=self.head.next
        if self.head is None:
            print("Oops! there is no element! ")
            return
    def printing(self):
        cur=self.head
        while cur:
            print(cur.data,end=" ")
 