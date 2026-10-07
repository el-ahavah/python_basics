# Class: A blueprint or template used to define what data an object can have and what actions it can perform. For example, a Person class can define that people have a name and age and can introduce() themselves.

# Object: A specific instance created from a class. Each object can have its own data. For example, person1 = Person("John", 20) creates an object called person1 from the Person class.

# Method: A function defined inside a class that describes an action or behavior associated with objects of that class. For example, introduce() can be a method of the Person class.

# __init__ method: A special method that Python automatically calls when a new object is created. It is commonly used to set up the object's initial attributes, such as its name and age.

"""
class Person:

    def __init__(self, name, age):   # __init__ method
        self.name = name
        self.age = age

    def introduce(self):             # method
        print(f"My name is {self.name}")


person1 = Person("John", 20)          # object
"""