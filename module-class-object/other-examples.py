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
