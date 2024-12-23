a = "Good"
b = "Bye"

print(a+b)
print(a,b) # , is a space.
print(a,b, end = " ") # end = " " makes it not skip line
print(b)

# It only prints so returns None
def foo(a, b) -> None:
    global x # Global must be in the function.
    x = x + 2
    print(a, b)

# Both are valid ways of calling a function.
x = 1
foo(b = "Hello", a = "World")
foo("Hello", "World")
print(x) # return 5 as 1 + 2 + 2 = 5.

# Data field in this class is a and b. c is a local data. 
class A:  
    # The self parameter must be the first parameter of every instance method of a class.
    def __init__(self):
        self.a = 1
        self.foo()
    def foo(self):
        c = 1
        self.b = 1

class B: 
    def __init__(self):
        self.one = 1
        self._two = 2
        self.__three = 3 # Name mangling happens here where it becomes _B__three.
        
    def public(self):
        print("public")
    
    def _conv_private(self):
        print("signal that this is private to the reader")
    
    def __private(self):
        print("acutally private through name mangling")
        
underscore = B()
print(underscore.one, underscore._two, underscore._B__three)
underscore.public()
underscore._conv_private()
underscore._B__private()


# Define a class named Dog
class Dog():
    # Constructor (__init__) initializes the instance's attributes when the object is created.
    def __init__(self, age: int, color: str):
        # Attribute: age of the dog (an integer)
        self.age = age
        # Attribute: color of the dog (a string)
        self.color = color
    
    # Method: Determines the breed category based on the age and color of the dog.
    def breed(self) -> None:
        # Local variables (not attributes): lists containing colors
        one = ['black', 'white']  # Colors in group "one"
        two = ['red', 'yellow']  # Colors in group "two"
        
        # Conditional structure to determine breed category
        if self.age < 5:  # Check if the age is less than 5
            if self.color in one:  # Check if color is in group "one"
                print("This is A")
            if self.color in two:  # Check if color is in group "two"
                print("This is B")
        elif 5 <= self.age <= 10:  # Check if age is between 5 and 10 (inclusive)
            if self.color in one:  # Check if color is in group "one"
                print("This is C")
            if self.color in two:  # Check if color is in group "two"
                print("This is D")
        else:  # For age greater than 10
            print("This is E")

# Main execution block
if __name__ == "__main__":
    # Create an instance (which is also an object in Python) of the Dog class with age=5 and color='black'
    mine = Dog(5, 'black')
    # Call the breed method on the instance
    mine.breed()

# Runtime error as self.y is not defined.      
# class Foo:
#     def __init__(self, x):
#         self.x = x
#     def getAddition(self):
#         print(self.x + self.y)
#     def foo2(self):
#         self.y = 5
# foo = Foo(2)
# foo.getAddition()

import threading

def worker(y):
    print(x+y)

if __name__=="__main__":
    x = 1
    threading.Thread(args=(1,), target=worker).start()
