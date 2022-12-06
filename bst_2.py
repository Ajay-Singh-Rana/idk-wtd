class Node:
    def __init__(self,data=None):
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
        if(self.data == None):
            print('Tree empty..!')
        else:
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
            if(self.left):
                prev = self
                temp = self.left
                while(temp.right != None):
                    prev = temp
                    temp = temp.right
                prev.right = temp.left
                temp.left = self.left
                temp.right = self.right
                del self
                print(f'Deleted {item}')
                return temp
            elif(self.right):
                prev = self
                temp = self.right
                while(temp.left != None):
                    prev = temp
                    temp = temp.left
                # delink temp from prev
                prev.left = temp.right
                # set temp.left and temp.right
                temp.left = self.left
                temp.right = self.right
                del self
                print(f'Deleted {item}')
                return temp
            del self
            print(f'Deleted {item}')
            return Node()
        elif(item < self.data):
            if(self.left):
                self.left.delete(item)
            else:
                print(f'{item} not found in the tree')
        else:
            if(self.right):
                self.right.delete(item)
            else:
                print(f'{item} not found in the tree')
        return self


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
t = t.delete(8)
t.traverse()

