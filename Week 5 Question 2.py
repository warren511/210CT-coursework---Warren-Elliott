class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,n,x):
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x
        if self.head==None:
            self.head=self.trail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x

    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print ("List: ",",".join(values))

    def remove(self,n):
        if n.prev!=None:
            n.prev.next=n.next
        else:
            self.head=n.next
        if n.next!=None:
            n.next.prev=n.prev
        else:
            self.tail=n.prev

if __name__=='__main__':
               l=List()
               a=Node(4)
               b=Node(6)
               c=Node(8)
               d=Node(9)
               l.insert(None,a)
               l.insert(l.head,b)
               l.insert(l.head,c)
               l.insert(l.head,d)
               l.display()
               l.remove(d)
               l.display()
