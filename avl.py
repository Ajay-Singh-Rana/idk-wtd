# h3avren

class AVLTree:
    def __init__(self,item):
        self.data = item;
        self.left = None;
        self.right = None;
        self.height = 0

    def insert(self,item):
        if(item < self.data):
            if(self.left == None):
                self.left = AVLTree(item)
            else:
                self.left.insert(item)
        else:
            
