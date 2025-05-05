# Object-Oriented Programming (OOP) in Python

This repository provides a comprehensive guide to Object-Oriented Programming (OOP) concepts in Python, complete with examples and explanations. It is designed to assist beginners and intermediate developers in understanding and implementing OOP principles effectively.

---

## Table of Contents
- [Class](#class)
- [Object](#object)
- [Attributes](#attributes)
- [Methods](#methods)
- [Instance](#instance)
- [Self](#self)
- [Inheritance](#inheritance)
- [Method Overloading](#method-overloading)
- [Method Overriding](#method-overriding)
- [Polymorphism](#polymorphism)
- [Encapsulation](#encapsulation)
- [Name Mangling](#name-mangling)
- [Repository Structure](#repository-structure)
- [How to Run](#how-to-run)
- [Prerequisites](#prerequisites)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Class
A **class** is a blueprint for creating objects. It defines attributes and methods that objects instantiated from the class will possess.

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
```

## Object
An **object** is an instance of a class, representing a concrete entity with its own data attributes and methods.

### Example:
```python
person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
```

## Attributes
**Attributes** (or properties) are data members of a class that define an object's characteristics.

### Example:
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.brand)  # Output: Toyota
```

## Methods
**Methods** are functions defined within a class that describe the behaviors of an object and can manipulate its attributes.

### Example:
```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))  # Output: 8
```

## Instance
An **instance** is a specific object created from a class, embodying the class's attributes and methods.

### Example:
```python
# Refer to the Object example above
```

## Self
The **self** keyword represents the instance of a class, allowing access to its attributes and methods.

### Example:
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy")
print(dog1.bark())  # Output: Buddy says Woof!
```

## Inheritance
**Inheritance** allows a child class to inherit properties and behaviors from a parent class.

### Types of Inheritance:
- **Single Inheritance**: A child class inherits from one parent class.
- **Multiple Inheritance**: A child class inherits from multiple parent classes.
- **Multi-Level Inheritance**: A class inherits from a child class of another class.
- **Hierarchical Inheritance**: Multiple child classes inherit from one parent class.
- **Hybrid Inheritance**: A combination of multiple inheritance types.

### Example:
```python
class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!
```

## Method Overloading
**Method overloading** allows multiple methods with the same name but different parameters. Python does not support this natively but can achieve it using the `multipledispatch` package.

### Example:
```python
from multipledispatch import dispatch

class Math:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(str, str)
    def add(self, a, b):
        return a + b

math = Math()
print(math.add(5, 3))  # Output: 8
print(math.add("Hello, ", "World!"))  # Output: Hello, World!
```

## Method Overriding
**Method overriding** occurs when a subclass redefines a method from its parent class to provide a specific implementation.

### Example:
```python
class Parent:
    def show(self):
        return "This is the parent class."

class Child(Parent):
    def show(self):
        return "This is the child class."

child = Child()
print(child.show())  # Output: This is the child class.
```

## Polymorphism
**Polymorphism** enables methods in different classes to share the same name but exhibit different behaviors.

### Example:
```python
class Bird:
    def fly(self):
        return "Birds can fly."

class Penguin(Bird):
    def fly(self):
        return "Penguins cannot fly."

bird = Bird()
penguin = Penguin()
print(bird.fly())  # Output: Birds can fly.
print(penguin.fly())  # Output: Penguins cannot fly.
```

## Encapsulation
**Encapsulation** involves bundling data and methods into a single unit, restricting direct access to some components.

### Example:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
```

## Name Mangling
**Name mangling** ensures private attributes are inaccessible outside the class by prefixing them with double underscores.

### Example:
```python
class Example:
    def __init__(self):
        self.__private = "This is private"

    def get_private(self):
        return self.__private

obj = Example()
print(obj.get_private())  # Output: This is private
```

## Repository Structure
```
OOPS-main/
├── Class_Object_Self.py
├── Single_Inheritance.py
├── Multiple_Inheritance.py
├── Multi_Level_Inheritance.py
├── Hierarchical_Inheritance.py
├── Hybrid_Inheritance.py
├── Method_Overloading.py
├── Method_Overriding.py
├── Name_Mangling.py
├── README.md
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/OOPS-main.git
   ```
2. Navigate to the project directory:
   ```bash
   cd OOPS-main
   ```
3. Run the Python files:
   ```bash
   python <filename>.py
   ```

## Prerequisites
- Python 3.x installed.
- Install the `multipledispatch` package for method overloading:
  ```bash
  pip install multipledispatch
  ```

## Contributing
Contributions are welcome! Fork the repository, make your improvements, and submit a pull request.

## License
This project is a course of work and not bound by a specific license.

## Author
Created by Naga Phanindra.
