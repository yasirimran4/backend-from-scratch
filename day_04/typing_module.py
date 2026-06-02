# Before Python 3.5 we do not know the type of a and b
from typing import List , Optional,Dict
def add(a, b): 
    return a + b

# After Python 3.5 we can use type hints to specify the expected types of a and b

def add_with_type(a :int,b:int) -> int:
    return a+b

def func() -> List[str]:
    return ["Hello", "World"]

def func_dict() -> Dict[str,str | int]:  # It's mean return type is either string or int , it is modern way to write union type
    return {"name": "yasir", "age": 20}

def func_optional() -> Optional[str]:  # It's mean return type is either string or None
    return None


# print(add_with_type(1, 2))  # Output: 3
# print(func())  # Output: ['Hello', 'World']


# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added. Modules are a way to organize code into reusable components. They can contain functions, classes, and variables that can be imported and used in other Python files.

# Python dataclasses are a way to define classes that are primarily used to store data. They provide 
# a convenient syntax for defining classes with attributes and automatically generate 
# methods like __init__, __repr__, and __eq__. Dataclasses can be used to create simple classes
#  that are easy to read and maintain, especially when dealing with data structures.

from dataclasses import dataclass , field

@dataclass
class Person:
    name: str
    age: int    

person = Person(name="Yasir", age=20)
person1 = Person(name="Esam", age=20)
print(person,person1)  # Output: Person(name='Yasir', age=20)    

# # This is same as
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age})"\


# Why Dataclasses Are Useful

# Very useful for:

# DTOs
# API schemas
# config objects
# response models
# backend architecture
# immutable objects
# clean code


@dataclass
class User:
    hobbies: list

    # hobbies is a mutable type (list), so we use default_factory to ensure that each instance of User gets its own separate list of hobbies. If we were to use hobbies: list = [] directly, all instances of User would share the same list, which could lead to unexpected behavior when modifying the hobbies of one user affecting all users.
user = User(hobbies=[])
t1 = User(hobbies=[])
t2 = User(hobbies=[])

t1.hobbies.append("Reading")
t1.hobbies.append("learning")
t2.hobbies.append("Gaming")
print(t1)  # Output: User(hobbies=['Reading'])
print(t2)  # Output: User(hobbies=[]) - t2's hobbies remain