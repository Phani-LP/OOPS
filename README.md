# OOPS
## Class: 
A class is blue print. It have methods, attributes, constructor function, etc.,
## Object:
Object: An object is an instance of a class. It is a concrete realization of the class, with its own unique data attributes and, potentially, modified behavior through its methods.

## Attributes: 
Also known as properties or fields, attributes are the data members of a class that define the characteristics of an object.

## Methods: 
Methods are functions associated with a class. They define the behavior of the class and can operate on the data attributes of the object.
## Instance:
An instance, also known as an object, is a concrete occurrence of a class. It represents a specific entity with its own set of attributes and can perform actions as defined by the methods in the class.
## Self: 
## Inheritance:
Inherting the properties one class to another class is nothing but inheritance.
Types:
1). Single Inheritance:

## Method Overloading: 
### Same method name but the difference is in the number of parameters or different datatypes of parameters or both is called "Method Overloading". 
We can't directly use method overloading in python. To use it we have to install "multipledispatch" package.
To use multipledispatch, you need to install the package first. You can do this using a package manager like pip:  pip install multipledispatch<br>
## Features of method overloading: 
Flexibility, Readability, Program Complexity decrease.

## Method Overriding:
Same method in super class and subclass with same parameters and 
we access the method in the subclass without accessing the super class
method this is nothing but method overriding.

### Rules for method overriding: 
1). Inheritance should be there.<br>
2). Same method and same parameters must be there in the super and sub class.<br>
3). Logic must be different in methods of super and subclass.<br>

## Polymorphism
The polymorphism is a Greek word. "POLY" means "MANY" and "MORPHISM" means "FORM" => Many Forms.
Definition: 
The ability to do more than one task is polymorphism.<br>
Examples: , Method Overriding, etc.,
### Types: Static Polymorphism & Dynamic Polymorphism
<h4>Static Polymorphism or Compile Time Polymorphism:</h4> If the polymorphism occurs during compilation of the program then it is called Static Polymorphism.<br>


<h5>Examples:<br> Operator Overloading:</h5> 
The operator "+" can be used for "addition of two numbers", "concatination of strings".<br>
The operator "*" can be used for "multiplication", "repetition", "packing & unpacking of arguments".
<h5> Method Overloading:</h5>
The print(), max(), min(), sorted(), etc., all the functions are examples for polymorphism.<br>
<h4>Dynamic Polymorphism or Run Time Polymorphism:</h4> If the polymorphism occurs during execution of the program then it is called Dynamic Polymorphism.:
Example: Method Overriding

### Encapsulation:
desc

## Name Mangling: 
Name Mangling can be used to access private data or methods in { own class objects, subclasses & subclass objects }.
Rule: Min 2 underscores before and maximum one underscore after the name of data or method. Ex: __data_, __data, ___data, ect.,














