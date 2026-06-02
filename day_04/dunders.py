# Important Dunder Methods

# "Dunder" = double underscore methods.

# They control Python object behavior.

class Iterator:
    def __init__(self, data):   # The __init__ method is a special method in Python classes that is called when an instance of the class is created. It is used to initialize the attributes of the class. In this case, it takes a parameter data and assigns it to self.data, and also initializes self.index to 0. This sets up the initial state of the iterator object.
        self.data = data
        self.index = 0
 
    def __iter__(self):        # This method is called when an iterator is initialized. It returns the iterator object itself. In this case, it simply
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        
my_list = [1, 2, 3]
iterator = Iterator(my_list)
for item in iterator:
    print(item)  # Output: 1, 2, 3        


class Test:
    def __init__(self, name):
        self.name = name

    def __str__(self):  # The __str__ method is a special method in Python that is called when you use the str() function on an object or when you print an object. It should return a string representation of the object. In this case, it returns a string that includes the name attribute of the Test class.
        return f"Test(name='{self.name}')"
    
t1 = Test("Yasir")
t1.name = "Esam"
print(t1)  # Output: Test(name='Esam')    