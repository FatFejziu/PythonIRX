class Student:
    def __init__(self, name, age, course, notaMesatare):
        self.name=name
        self.age=age
        self.course=course
        self._notaMesatare=notaMesatare
    def greet(self):
        print(f"Hello, I am {self.name}, I am {self.age} and I am studying {self.course}")

    def _tregonota(self):
        print("This is a protected Method")

Fat=Student("Fat",16,"Python")
Luan=Student("Luan",17,"FullStack")
Arlind=Student("Arlind",17,"Devops")

Luan.greet()