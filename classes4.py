class Dog(object):
    dogs=[]
    def __init__(self,name):
        self.name=name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)
    @staticmethod
    def bark(n):
        for _ in range(n):
            print("Bark")

class Math:
    @staticmethod
    def add(x,y):
        return x+y