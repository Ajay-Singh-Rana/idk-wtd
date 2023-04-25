# h3avren

import random

class Node:
    def __init__(self, value, symbol = 'H'):
        self.data = value
        self.left = None
        self.right = None
        self.symbol = symbol

    def __str__(self):
        return f'<data = {self.data}\n left = {self.left}\n right = {self.right}>'

    def __repr__(self):
        return f' {self.data} '

    def insert(self, data_item_1, data_item_2):
        if(self.left == None and self.right == None):
            self.left = Node(data_item_1, symbol = 'L')
            self.right = Node(data_item_2, symbol = 'R')
        else:
            choice = random.randint(0,1)
            if(choice):
                self.left.insert(data_item_1, data_item_2)
            else:
                self.right.insert(data_item_1, data_item_2)

    def traverse(self):
        if(self.data == None):
            print("empty")
        else:
            print(self.data, self.symbol)
            if(self.left):
                self.left.traverse()
            if(self.right):
                self.right.traverse()
            
t = Node(5)
t.insert(6,7)
t.insert(8,9)
t.insert(10,11)
t.traverse()
