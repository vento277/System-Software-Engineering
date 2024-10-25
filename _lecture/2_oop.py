"""
Values and operations permitted on a variable are determined by its type (or data type).

An object is a variable with both data (attributes) and functions (methods), allowing it to manipulate its own data.

A class is a blueprint for creating objects. An object created from a class has a type that is defined by the attributes and methods of the class.
    - Objects like strings are immutable, meaning they cannot be changed once instantiated.
    - Objects like lists are mutable, meaning they can be changed after creation.

For example:
    msg = "Hello"
    print(msg[0]) works because it's indexing the string, retrieving the character at position 0.
    However, attempting to modify it using:
    msg[0] = "J" results in a TypeError because strings are immutable. 
    This kind of indexing or assignment works with mutable types like lists or dictionaries.
"""

# This is a parent class
class Person:
    def __init__(self):
        self = self

# This is a child class. It can inherit attributes and methods from the parent class.
class Gender(Person):
    def __init__(self):
        self = self

    # A method that uses another class as an argument is a class method.
    def sub(self, person: Person):
        pass

class BMI:
    """ This class defines the BMI type.
        Data fields (attributes): __name, __weight, __height. These are instance variables, which belong to the object created from the class.
        Methods (functions): __init__, getBMI, getStatus
    """

    # Class attribute. This is shared across all instances of the class.
    shared = 'WOW'

    # Initializer. It creates the object's instance variables (data fields).
    # "__" before a variable triggers name mangling, making it private to the class.
    def __init__(self, name: str, weight: float, height: float):
        # 'self' refers to the instance of the object being created. It is a convention not a keyword. 
        
        # "_" signals that a variable is intended to be private, though this is not enforced by Python.
        self._name = name
        self.__weight = weight
        self.__height = height

    # A method that uses 'self' refers to instance variables and is called an instance method.
    def getBMI(self) -> float:
        K_per_LB = 0.4539
        m_per_in = 0.0254
        bmi = self.__weight * K_per_LB / \
              ( (self.__height * m_per_in) * \
                (self.__height * m_per_in))
        
        return round(bmi * 100) / 100  # Rounding to two decimal places

    def getStatus(self) -> str:
        bmi = self.getBMI()
        if bmi > 25:
            return self._name + " is Overweight"
        elif 18.5 <= bmi <= 25:
            return self._name + " is Normal weight"
        else:
            return self._name + " is Underweight"

    # A function that doesn't interact with any instance variables is called a static method.
    @staticmethod
    def static(arg1, arg2):
        pass

if __name__ == "__main__":
    
    # Instantiation. Creates an object of the type defined by the class.
    p1 = BMI("John Doe", 145, 70)

    # Calling methods from the instance.
    bmi1 = p1.getBMI()
    status1 = p1.getStatus()

    print(bmi1, status1)
