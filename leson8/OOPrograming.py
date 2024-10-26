class Rectangle: #defined a class
    def __init__(self, length, width): #konstruktori i klases (self)
        self.length=length
        self.width=width
    def calculate_arena(self):
        return self.length*self.width
    def calculate_perimeter(self):
        return 2*(self.length+self.width)

katroti=Rectangle(2,5)

syprina=katroti.calculate_arena()
print(syprina)