class Node:
    def __init__(self,datavale=None):
        self.dataval = datavale
        self.nextval = None

class SLikedList:
    def __init__(self):
        self.headval = None 

    def listprint(self):
        pritnval = self.headval
        while pritnval is not None:
            print (pritnval.dataval)
            pritnval = pritnval.nextval

    def atbegining(self,newdata):
        NewNode = Node(newdata)


        NewNode.Nextval = self.headval
        self.headval = NewNode



list1 = SLikedList()
list1.headval = Node('mon')
e2 = Node('tue')
e3 = Node('wed')
e4 = Node('tue')
e5 = Node('friday')
e6 = Node('sat')
e7 = Node('sun')
list1.headval.nextval = e2 

e2.nextval = e3 
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6
e6.nextval = e7 

list1.atbegining('sun ')

list1.listprint()