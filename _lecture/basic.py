'''
Operating system manages and allocates resources for programs, including memory and processing power.
It acts as an intermediary between the user and the computer.
It also provides an environment in which a user can execute programs. 

Real-time systems implies that the function of the code is time-sentitive and involove scheduling.
Hard real-time systems are thoes that require a task to be done before the deadline. 
Soft real-time systems are thoes that wants a task to be done before the deadline. 

Python is an interpreted languages. Meaning that it executes instructions directly, without the need for a compilation.

The coding style should follow: https://peps.python.org/pep-0008/

# -> is for a comment on a block of code or a line
'''''' -> is for a documentation comment for a function or a module.

Python is case sensitive with regards to their variable naming.
Python dosen't require a declaration beforehand for one to use the variable. The type is inferred from the usage.

Python is dynamically typed, meaning variables can change type during runtime. Unlike statically typed languages like C, 
Python determines variable types at runtime rather than at compile-time. This flexibility is managed by Python's runtime environment.
To better declare a variable, one can hint the IDE what the variable type may be.
Type hints improve code readability and help with debugging, but they are not enforced by Python.

The scope of variable is important. Variable scope refers to the region of the code where a variable is accessible and valid. 

Indentation is how python notices blocks of codes. Therefore, it is needed to be done correctly unlike C-based languages.

Functions use the def keyword to define/create the function/method. Keyword is a word that serves specific function in Python, 
and cannot be set as a variable name. It is built-in. 

Modules are collection of definitions, such as functions, classes and variables. 
Modules can be imported. This is done using the keyword 'import', which imports the whole module 
or 'from import' which imports a specific function from the module.

Python operators are simple. But there is '**' which represents exponentiation, and '//' which represents the floor division. 
One can also use 'is' and 'in' which is the identity and membership operator.

Python also has a function that allows it to know if it is being run locally or ran imported. 
if__name__ == "__main__".

Graceful error handling is crucial for robust code. Use exceptions to manage potential errors, 
but be cautious as handling exceptions can be costly in terms of performance.
Only use broad exception handling if you are certain that specific errors are expected and need to be managed.
'''
# Note that we can use both "" and ''. The difference in its useage comes from the need of '' in the sentences.
# If the printed word needs '', "" should be used. Otherwise, use ''.
print("Hello World")
print('Hello World')

# Hinting the variable type and function's return values
grade: int = 1
text: str = "Excellent"

# k=z does not create a new list. k becomes a reference to z. So any change in k affects z as well. 
z = [0, 1]
k = z
k.append(3)
print(f"{z} {k}")

def func1() -> None:
    print('Hint')
    
def func2(a:float, b:float) -> None:
    print(a + b)
    
func1()
func2(1.1, 2)

# The variable scope of function foo only changes x locally since x is not delcared global within. 
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

# Indentation must follow after the loop or statements.
for i in range(3):
    print('A')

for _ in range(3): # This is also a valid way of declaring a loop.
    print('C')

y = 2
if y >= 0:
    print('B')

# Lists can store a collection of data of any size.
list1 = []
list2 = ['Red','Green']

if __name__ == "__main__":
    print('Main Process')

# Exception Handling
def exception1():
    try: 
        x = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.") # Handle the case where the input cannot be converted to an integer

def exception2():
    try: 
        x = int(input("Enter an integer: "))
        print(1 / x)  # Attempt to divide by the user-provided integer
    except ZeroDivisionError:
        # Handle the case where the user provides zero, causing a division by zero error
        print("Division by zero is not allowed.")
    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        # Catch all other exceptions and print a generic error message along with the exception details
        print(f"An unexpected error occurred: {e}")

# In this example, `x` is recognized within the nested function `foo` even though it's defined outside of it. This is because when modifying 
# a mutable object like a list (using .append), Python directly modifies the original object, unlike reassigning `x` with something like `x = 1`.
def var_range():
    x = [1, 2]
    def foo():
        x.append(2345)  # Modifies the original list `x`
        print(x)        # Prints: [1, 2, 2345]
    foo()
    print(x)            # Also prints: [1, 2, 2345] since the original list was modified

# There is a pythonic way for writing a code. It reduces multiple lines to codes to only a few.
# But it often de-greades the readability. So over-use of it is not encouraged.
# Normal way.
lst = list()
for i in range(1, 4):
    lst.append(i)
print(lst)

# More Pythonic way
lst = [(i+1) for i in range(1,4)]
print(lst)

lst = [(i+1) for i in range(1,4) if i%2 == 0] # It can also be conditional
print(lst)

[print(i, end = "") for i in range(0,3)] # Whatever print returns goes into the list. Not the best readability.

