# h3avren

class List:
    """Just an iterator"""

    def __init__(self, start = 0, stop = None, step = 1):
        if (stop == None):
            self.current = 0
            self.stop = start
        else:
            self.current = start
            self.stop = stop
        self.step = step
        self.return_list = list([self.current])
       

    def __iter__(self):
       return self

    def __next__(self):
        temp = self.return_list
        if(self.current == self.stop):
            raise StopIteration
        self.current += self.step
        self.return_list.append(self.current)
        return self.return_list

# list_ = List(3)
for i in List(4,10):
    print(i)

"""
list_ = iter(list_)
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))
print(next(list_))"""
