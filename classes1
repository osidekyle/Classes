class Dog(object):
    def __init__(self,name, age):
        self.name=name
        self.age=age
        print('Nice you made a dog')

    def speak(self):
        print("Hi i am "+self.name+" and I am",self.age,"years old")

    def talk(self):
        print("Bark")
class Cat(Dog):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
        self.name='tim'
    def talk(self):
        print("Meow")

tim=Cat("kyle",20,'white')
tim.speak()
tim.talk()
