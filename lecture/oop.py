"""
Type is a set of values and operations permitted on the value.
Class is a way to create this type.
"""

class BMI:
    """ This class defines the BMI type.
        data fields: __name, __weight, __height. These are data that a type depends on. These are not local variables.
        methods: init, getBMI, getStatus
    """

    # This is a shared variable which is given to every object that instanciates this class.
    shared = 'WOW'

    def __init__(self, name, weight, height):

        # "_" signals that it is meant to be private to the reader, but not enforced by the program.
        # "__" is name mangling - making the data field to be a private. 
        self.__name = name
        self.__weight = weight
        self.__height = height

    def getBMI(self) -> float:
        K_per_LB = 0.4539
        m_per_in = 0.0254
        bmi = self.__weight * K_per_LB / \
        ( (self.__height * m_per_in) * \
         (self.__height * m_per_in))
        
        return round(bmi * 100) / 100

    def getStatus(self) -> str:
        bmi = self.getBMI()
        if bmi > 20:
            return self.__name + " is Overweight"
        elif 20 <= bmi <= 15:
            return self.__name + " is Average-weight"
        else:
            return self.__name + " is Underweight"

if __name__ == "__main__":
    
    # Instanciation. Creates an object of the type defined by the class.
    bmi1 = BMI("John Doe", 145, 70)
    print(bmi1.getBMI()) 
    print(bmi1.getStatus())

    # Mutable are changable objects, ex. lists 
    # Inverse is immutable, ex. string. So if the program has to deal with thousands of strings, it will be compute expensive. 
    