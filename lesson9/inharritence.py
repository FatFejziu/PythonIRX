class Animal:
    def __init__(self,name):
        self.name=name


    def sound(self):
        print("Some generic animal sound")
    def description(self):
        print(f"This animal;s name is {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed


    def sound(self):
        print("Woof! Woof!")

    def description(self):
        super().description()
        print(f"This is the breed {self.breed}")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print("Meow! Meow!")

kafsha=Animal("generic name")
kafsha.sound()

qeni=Dog("Rex", "Golden Retriver")
qeni.sound()

maca=Cat("Whiskers")
maca.sound()