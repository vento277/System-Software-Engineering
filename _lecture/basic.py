# Introduction
# Review the official Python documentation for in-depth information about Python's features and the code base. While Python's documentation may not always be perfect, 
# it remains one of the best resources available for understanding the language.

# Operating System
# The operating system manages and allocates resources for programs, including memory and processing power.

def function_name() -> None:
    """
    The '-> None' notation is a type hint indicating that this function does not return a value. 
    Type hints improve code readability and help with debugging, but they are not enforced by Python.
    """
    pass 

# Variable Scope
# Variable scope refers to the region of the code where a variable is accessible and valid. 
# Python is dynamically typed, meaning variables can change type during runtime. Unlike statically typed languages like C, 
# Python determines variable types at runtime rather than at compile-time. This flexibility is managed by Python's runtime environment.

# Exception Handling
# Graceful error handling is crucial for robust code. Use exceptions to manage potential errors, but be cautious as handling exceptions can be costly in terms of performance.
# Only use broad exception handling if you are certain that specific errors are expected and need to be managed.
def exception1():
    try: 
        x = int(input("Enter an integer: "))
    except ValueError:
        # Handle the case where the input cannot be converted to an integer
        print("Invalid input. Please enter a valid integer.")

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

# In this example, `x` is recognized within the nested function `foo` 
# even though it's defined outside of it. This is because when modifying 
# a mutable object like a list (using .append), Python directly modifies 
# the original object, unlike reassigning `x` with something like `x = 1`.
def var_range():
    x = [1, 2]
    def foo():
        x.append(2345)  # Modifies the original list `x`
        print(x)        # Prints: [1, 2, 2345]
    foo()
    print(x)            # Also prints: [1, 2, 2345] since the original list was modified
    