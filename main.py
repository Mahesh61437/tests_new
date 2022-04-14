#  classes

# syntax

# class ClassNameV1:

def tell_age():
    print("from normal function")


class Person:
    name: str
    gender: str
    age: int

    def __init__(self, n, a, g="M"):
        self.name = n
        self.age = a
        self.gender = g

    def speak(self):
        print(f"hi my name is {self.name} ")

    def tell_age(self):
        print(f"Person: my age is {self.age} ")

    def send_name(self):
        return self.name


obj = Person("Mahesh", 24)

#  oops
# Classes
# objects
# inheritance
# polymorphism
# encapsulation
# abstraction


# inheritance

class Employee(Person):
    id: str
    salary: int
    company_name: str

    def __init__(self, name, age, gender, id, salary,  company_name):
        super().__init__(name, age, gender)
        self.id = id
        self.salary = salary
        self.company_name = company_name

    def details(self):
        print(self.id, self.salary, self.company_name)


emp1 = Employee("mahesh", 24, "M", id="1234", salary="50000", company_name="Wipro")

emp1.details()

emp1.tell_age()
