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
#-----------------------------------------------------------------
"""
class Person:
    # This runs whenever we create a new Person object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This is a method
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    # Another method
    def birthday(self):
        self.age = self.age + 1
        print(f"Happy birthday! I am now {self.age} years old.")


# Create objects from the Person class
person1 = Person("John", 20)
person2 = Person("Mary", 25)


# Access the objects' attributes
print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)


# Call the objects' methods
person1.introduce()
person2.introduce()


# Change person1's age
person1.birthday()

# Check the new age
print(person1.age)
"""
#--------------------------------------------------------------------
"""
# inheritance
class Animal:
    def speak(self):
        print("Animals make sounds")


class Dog(Animal):
    pass


class Cat(Animal):
    def speak(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
"""
#------------------------------------------------------------
"""
class Parent:
    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")

        super().altered()

        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()
"""
#-----------------------------------------------------------------
"""
class Parent:
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super().altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
"""
#---------------------------------------------------------------------------

class Other:
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")


class Child:
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()