class Parent:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("im parent")

class Child(Parent):

    def speak(self):
        print("im child")

    def tell_name(self):
        print(self.name)


class GrandChild(Child):

    gender: str

    def speak(self):
        super(Child, self).speak()
        super().speak()
        print("im grand child")

    def tell_age(self):
        print(self.age)


p = Parent(age=24, name="mahesh")
c = Child(age=24, name="mahesh")
gc = GrandChild(age=24, name="mahesh")

p.speak()
c.speak()
gc.speak()

