# class Person:
#     # This runs whenever we create a new Person object
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # This is a method
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

#     # Another method
#     def birthday(self):
#         self.age = self.age + 1
#         print(f"Happy birthday! I am now {self.age} years old.")


# # Create objects from the Person class
# person1 = Person("John", 20)
# person2 = Person("Mary", 25)


# # Access the objects' attributes
# print(person1.name)
# print(person1.age)

# print(person2.name)
# print(person2.age)


# # Call the objects' methods
# person1.introduce()
# person2.introduce()


# # Change person1's age
# person1.birthday()

# # Check the new age
# print(person1.age)

#--------------------------------------------------------------------------

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def describe(self):
        print(f"This car is a {self.year} {self.brand} {self.model}.")

    def accelerate(self, amount):
        self.speed = self.speed + amount
        print(f"The car is now moving at {self.speed} km/h.")

    def stop(self):
        self.speed = 0
        print("The car has stopped.")


# Create an object from the Car class
my_car = Car("Toyota", "Corolla", 2022)


# Access the object's attributes
print(my_car.brand)
print(my_car.model)
print(my_car.year)


# Use the object's methods
my_car.describe()

my_car.accelerate(20)
my_car.accelerate(30)

my_car.stop()