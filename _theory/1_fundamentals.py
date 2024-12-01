'''
Python is an interpreted language, meaning it executes instructions directly 
without the need for compilation.

The coding style should follow: https://peps.python.org/pep-0008/

# -> is for a comment on a block of code or a line
''' ''' -> is for a documentation comment for a function or a module.

Python is case-sensitive regarding variable naming and it cannot start with a digit. 
Python doesn't require a declaration beforehand for variable use - the type is inferred from usage.

Python is dynamically typed, meaning variables can change type during runtime. 
Unlike statically typed languages like C, Python determines variable types at runtime rather than at compile-time. This flexibility is managed by Python's runtime environment. 
To better declare a variable, one can hint the IDE about the variable type.
Type hints improve code readability and help with debugging, but they are not enforced by Python.

The scope of a variable is important. Variable scope refers to the region of the code where a variable is accessible and valid.

Indentation is how Python notices blocks of code. Therefore, it must be done correctly, unlike C-based languages.

Functions use the `def` keyword to define/create the function/method. 
A keyword is a word that serves a specific function in Python and cannot be set as a variable name.
A boolean literal is a word that serves as a boolean. For example, the word True is both a keyword and a boolean 1.

Modules are collections of definitions, such as functions, classes, and variables. 
Modules can be imported using the `import` keyword, which imports the whole module, 
or `from import`, which imports a specific function from the module.

Python operators are simple. 
However, '**' represents exponentiation, and '//' represents floor division. 
You can also use 'is' and 'in' as identity and membership operators.

Python has a function that allows it to know if it is being run locally or imported: 
`if __name__ == "__main__":`.
This allows the program to be run locally or safely imported.

Graceful error handling is crucial for robust code. 
Use exceptions to manage potential errors, but be cautious, as handling exceptions can be costly in terms of performance. 
Only use broad exception handling if you are certain that specific errors are expected and need to be managed.

Identity operators 'is' and 'is not' can be used to check if two variables refer to the same object. 
This is difference to = and != as they only check the associated values. For example two $50 bills are same in their value but different
due to their serial numbers. 
'''
# Note that we can use both "" and ''. The difference in usage comes from the need for '' in the sentences. 
# If the printed word needs '', "" should be used. Otherwise, use ''.
print("Hello World")
print('Hello World')

name = "CPEN 333"
print(f"Course: {name}") # Print can also be formatted using f

# Python can also use ; to separate codes. But it is not considered a good style. 
print("This"); print("That")

# Hinting the variable type and function's return values.
grade: int = 1
text: str = "Excellent"

# Lists can store a collection of data of any size while maintaining order. They can be of any type as well. 
# Tuple is identical to list except for the fact that it is not mutable. 
list1 = []
list2 = ['Red', 'Green', 1]

a = []
a.append(1); a.append(2); a.append(1)
print(a)

# Sets can also store data of any size and type. But they are non-repeating and not placed in particular order. 
b = set()
b.add(1); b.add(2); b.add(1); b.add(2)
print(b)

# Dictionary stores data based on key-value pairs. 
c = {}
c[1] = "One"; c[2] = "Two"; c[3] = "Three"
print(c)

print(a[1], c[1])

# Indentation must follow after the loop or statements.
for i in range(3):
    print('A')

for _ in range(3):  # This is also a valid way of declaring a loop.
    print('C')

y = 2
if y >= 0:
    print('B')

# If statements can be used is various ways.
something = True
if something: # Executes if something is true.
    print("True")

elif something is True:
    print("True")

elif not something: # Executes if something is false.
    print("False")

elif something is False:
    print("False")

else:
    print("False")

# k=z does not create a new list. k becomes a reference to z. 
# Therefore, any change in k affects z as well. 
z = [0, 1]
k = z
k.append(3)
print(f"{z} {k}")

def func1() -> None:
    print('Hint')
    
def func2(a: float, b: float) -> None:
    print(a + b)
    
func1()
func2(1.1, 2)

# The variable scope of function foo only changes x locally since x is not declared global within. 
# As a result, the function outputs '454'.
global x
def foo():
    x = 5
    print(x, end="")
    x = x + 1

x = 4
print(x, end="")
foo()
print(x)


# Exception Handling
def exception1():
    try: 
        x = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")  # Handle the case where the input cannot be converted to an integer

def exception2():
    try: 
        x = int(input("Enter an integer: "))
        print(1 / x)  # Attempt to divide by the user-provided integer
    except ZeroDivisionError:
        print("Division by zero is not allowed.")  # Handle division by zero error
    except ValueError:
        print("Invalid input. Please enter a valid integer.")  # Handle invalid integer input
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Catch all other exceptions
    else:
        print("No exeception raised")
    finally:
        print("Always print")

with something: # is the same as...
    pass 

try: #...
    pass
finally:
    pass

# In this example, `x` is recognized within the nested function `foo` 
# even though it's defined outside of it. 
# This is because when modifying a mutable object like a list (using .append), 
# Python directly modifies the original object.
def var_range():
    x = [1, 2]
    def foo():
        x.append(2345)  # Modifies the original list `x`
        print(x)        # Prints: [1, 2, 2345]
    foo()
    print(x)            # Also prints: [1, 2, 2345] since the original list was modified

# There is a Pythonic way of writing code that reduces multiple lines of code to only a few.
# However, it often degrades readability, so overuse is not encouraged.
# Normal way.
lst = list()
for i in range(1, 4):
    lst.append(i)
print(lst)

# More Pythonic way
lst = [(i + 1) for i in range(1, 4)]
print(lst)

lst = [(i + 1) for i in range(1, 4) if i % 2 == 0]  # Conditional list comprehension
print(lst)

[print(i, end="") for i in range(0, 3)]  # Not the best readability, as print returns goes into the list.

