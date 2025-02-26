class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ahmed", 24)

print(f"The person name is {p1.name} and he is {p1.age} years old")

print(p1)

#the example below is a class with __str__ representation
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"
p2 = Person2("Loyal", 24)

print(p2)

#here is an example of using inheritance.
class Student(Person):
    #use pass statement when you don't intend to include any method or object in the class
    pass

s1 = Student("Opeyemi", 25)
print(f"The first student name is {s1.name} and the student is {s1.age} years old")

