class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,value):
        if(value<self.data):
            if(self.left == None):
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if(self.right == None):
                self.right = Node(value)
            else:
                self.right.insert(value)

    def traverse(self):
        if(self.left):
            self.left.traverse()

        print(self.data)

        if(self.right):
            self.right.traverse()
    
    def search(self,item):
        if(self.data == item):
            print(item,"found..!")
        elif(item < self.data):
            if(self.left):
                self.left.search(item)
            else:
                print(item,"not found..!")
        elif(item > self.data):
            if(self.right):
                self.right.search(item)
            else:
                print(item,"not found..!")

    def delete(self,item):
        if(self.data == item):
            temp = self


t =  Node(5)
t.insert(7)
t.insert(2)
t.insert(3)
t.insert(1)
t.insert(9)
t.insert(8)
t.search(3)
t.search(8)
t.search(6)
t.insert(6)
t.traverse()

