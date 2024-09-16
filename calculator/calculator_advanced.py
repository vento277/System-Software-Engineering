#Lab 2 (part1)
#student name: Peter Kim
#student number: 18693002

from tkinter import *
#do not import any more modules

#do not change the skeleton of the program. Only add code where it is requested.
class Rational:
    """ this class implements the rational number type 
        it stores the rational number in its lowest from
        two data fields: 
            numerator and denominator
            (numerator stores the sign of the rational)
        Operation: 
            add, subtract, multiply and divide
            toString
    """
    def __init__(self, numerator: int, denominator: int) -> None:
        """initizer stores the rational number in the lowest form""" 
        def greatestCommonDivisor(n: int, d: int):
            """inner function for the greatest common divisor calculation"""
            n1 = abs(n)
            d1 = abs(d)
            result = 1
            k=1
            while k <= n1 and k <= d1:
                if n1 % k == 0 and d1 % k == 0:
                    result = k
                k += 1
            return result
        #rational number must be in the lowest form 
        gcd: int = greatestCommonDivisor(numerator, denominator)
        #numerator stores the sign of the rational
        signFactor: int = 1 if denominator > 0 else -1
        self.numerator = signFactor * numerator // gcd
        self.denominator = abs(denominator) // gcd
    
    def add(self, secondRational):
        """adds 'this' rational to secondRational
           returns the result as a rational number (type Rational)
        """  
        # r1 = a/b r2 = c/d; r1 + r2 = [(a*d) + (b*c)] / (b*d) 
        numerator  = ((self.numerator * secondRational.denominator) + (self.denominator * secondRational.numerator))
        denominator = (self.denominator * secondRational.denominator)
        number = Rational(numerator, denominator) # return the result as type Rational
        return number
    
    def subtract(self, secondRational):
        """subtracts secondRational from 'this' rational to 
           returns the result as a rational number (type Rational)
        """ 
        # r1 = a/b r2 = c/d; r1 + r2 = [(a*d) - (b*c)] / (b*d) 
        numerator  = ((self.numerator * secondRational.denominator) - (self.denominator * secondRational.numerator))
        denominator = (self.denominator * secondRational.denominator)
        number = Rational(numerator, denominator) # return the result as type Rational
        return number

    def multiply(self, secondRational):
        """multiplies 'this' rational to secondRational
           returns the result as a rational number (type Rational)
        """ 
        # r1 = a/b r2 = c/d; r1 + r2 = (a*c) / (b*d) 
        numerator  = (self.numerator * secondRational.numerator)
        denominator = (self.denominator * secondRational.denominator)
        number = Rational(numerator, denominator) # return the result as type Rational
        return number

    def divide(self, secondRational):
        """divides 'this' rational by secondRational
           returns the result as a rational number (type Rational)
        """ 
        # r1 = a/b r2 = c/d; r1 + r2 = (a*d) / (b*c) 
        numerator  = (self.numerator * secondRational.denominator)
        denominator = (self.denominator * secondRational.numerator)
        number = Rational(numerator, denominator) # return the result as type Rational
        return number

    def toString(self):
        """ returns a string representation of 'this' rational
            the format is: numerator/denominator
            if 'this' rational is an integer, it must not show any denominator 
            if denominator is 0, it just returns "NaN" (not a number)
        """ 
        if self.denominator == 0:
            return "NaN" # If the denominator is zero, return "NaN" to indicate that the fraction is undefined
        else:
            if self.numerator == self.denominator:
                return '1' # If the numerator is equal to the denominator, return '1' because the fraction represents 1
            elif (self.denominator == 1) or (self.numerator == 0):
                # If the denominator is 1, or the numerator is 0, return the numerator as a string
                # - If the denominator is 1, the fraction simplifies to just the numerator (e.g., 3/1 is just 3)
                # - If the numerator is 0, the fraction simplifies to 0 (e.g., 0/5 is just 0)
                return str(self.numerator)
            else:
                return str(self.numerator) + "/" + str(self.denominator) # For all other cases, return the fraction in the format "numerator/denominator"

class Imaginary:
    """ this class implements the imaginary number type 
        it stores the imaginary number
        two data fields: 
            real and imaginary
        Operation: 
            add, subtract, multiply and divide
            toString
    """
    
    def addComplex(self, secondImaginary):
        pass
    def substractComplex(self, secondImaginary):
        pass
    def multiplyComplex(self, secondImaginary):
        pass
    def divideComplex(self, secondImaginary):
        pass

class GUI:
    """ this class implements the GUI for our program
        use as is.
        The add, subtract, multiply and divide methods invoke the corresponding
        methods from the Rational class to calculate the result to display.
    """
    def __init__(self):
        """ The initializer creates the main window, label and entry widgets,
            and starts the GUI mainloop.
        """
        window = Tk()
        window.title("RN & CN") #Rational Numbers & Complex Numbers

        # Labels and entries for the first rational number
        frame1 = Frame(window)
        frame1.grid(row=1, column=1, pady=10)
        Label(frame1, text="Rational 1:").pack(side=LEFT)
        self.rational1Numerator = StringVar()
        Entry(frame1, width=5, textvariable=self.rational1Numerator,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)
        Label(frame1, text="/").pack(side=LEFT)
        self.rational1Denominator = StringVar()
        Entry(frame1, width=5, textvariable=self.rational1Denominator,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)

        # Labels and entries for the second rational number
        frame2 = Frame(window)
        frame2.grid(row=3, column=1, pady=10)
        Label(frame2, text="Rational 2:").pack(side=LEFT)
        self.rational2Numerator = StringVar()
        Entry(frame2, width=5, textvariable=self.rational2Numerator,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)
        Label(frame2, text="/").pack(side=LEFT)
        self.rational2Denominator = StringVar()
        Entry(frame2, width=5, textvariable=self.rational2Denominator,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)

        # Labels and entries for the result rational number
        frame3 = Frame(window)
        frame3.grid(row=4, column=1, pady=10)
        Label(frame3, text="Result:     ").pack(side=LEFT)
        self.result = StringVar()
        Entry(frame3, width=10, textvariable=self.result,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)

        # Buttons for add, subtract, multiply and divide
        frame4 = Frame(window)
        frame4.grid(row=5, column=1, pady=5)
        Button(frame4, text="Add", command=self.add).pack(side=LEFT)
        Button(frame4, text="Subtract", command=self.subtract).pack(side=LEFT)
        Button(frame4, text="Multiply", command=self.multiply).pack(side=LEFT)
        Button(frame4, text="Divide", command=self.divide).pack(side=LEFT)

        # The GUI has been updated to include an imaginary number calculator, which is now located beneath the previous calculator. New buttons have also been added.

        # New frames and entries for imaginary numbers
        frame5 = Frame(window)
        frame5.grid(row=6, column=1, pady=10)
        Label(frame5, text="Complex 1:").pack(side=LEFT)
        self.complex1Real = StringVar()
        Entry(frame5, width=5, textvariable=self.complex1Real,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)
        Label(frame5, text="+").pack(side=LEFT)
        self.complex1Imag = StringVar()
        Entry(frame5, width=5, textvariable=self.complex1Imag,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)
        Label(frame5, text="i").pack(side=LEFT)

        frame6 = Frame(window)
        frame6.grid(row=7, column=1, pady=10)
        Label(frame6, text="Complex 2:").pack(side=LEFT)
        self.complex2Real = StringVar()
        Entry(frame6, width=5, textvariable=self.complex2Real,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)
        Label(frame6, text="+").pack(side=LEFT)
        self.complex2Imag = StringVar()
        Entry(frame6, width=5, textvariable=self.complex2Imag,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)
        Label(frame6, text="i").pack(side=LEFT)

        # Result frame for complex numbers
        frame7 = Frame(window)
        frame7.grid(row=8, column=1, pady=10)
        Label(frame7, text="Complex Result:").pack(side=LEFT)
        self.complexResult = StringVar()
        Entry(frame7, width=15, textvariable=self.complexResult,
            justify=RIGHT, font=('Calibri 13')).pack(side=LEFT)

        # Buttons for complex number operations
        frame8 = Frame(window)
        frame8.grid(row=9, column=1, pady=5)
        Button(frame8, text="Add Complex", command=self.addComplex).pack(side=LEFT)
        Button(frame8, text="Subtract Complex", command=self.subtractComplex).pack(side=LEFT)
        Button(frame8, text="Multiply Complex", command=self.multiplyComplex).pack(side=LEFT)
        Button(frame8, text="Divide Complex", command=self.divideComplex).pack(side=LEFT)
               
        mainloop()
        
    def add(self): 
        (rational1, rational2) = self.getBothRational()
        result = rational1.add(rational2)
        self.result.set(result.toString())
    
    def subtract(self):
        (rational1, rational2) = self.getBothRational()
        result = rational1.subtract(rational2)
        self.result.set(result.toString())
    
    def multiply(self):
        (rational1, rational2) = self.getBothRational()
        result = rational1.multiply(rational2)
        self.result.set(result.toString())
    
    def divide(self):
        (rational1, rational2) = self.getBothRational()
        result = rational1.divide(rational2)
        self.result.set(result.toString())

    # 

    def addComplex(self):
        (imaginary1, imaginary2) = self.getBothRational()
        result = imaginary1.divide(imaginary2)
        self.result.set(result.toString())

    def subtractComplex(self):
        (imaginary1, imaginary2) = self.getBothRational()
        result = imaginary1.divide(imaginary2)
        self.result.set(result.toString())

    def multiplyComplex(self):
        (imaginary1, imaginary2) = self.getBothRational()
        result = imaginary1.divide(imaginary2)
        self.result.set(result.toString())

    def divideComplex(self):
        (imaginary1, imaginary2) = self.getBothRational()
        result = imaginary1.divide(imaginary2)
        self.result.set(result.toString())

    def getBothRational(self):
        """ Helper method used by add, subtract, multiply and divide methods"""
        try:
            numerator1 = eval(self.rational1Numerator.get())
            denominator1 = eval(self.rational1Denominator.get())
            rational1 = Rational(numerator1, denominator1)

            numerator2 = eval(self.rational2Numerator.get())
            denominator2 = eval(self.rational2Denominator.get())
            rational2 = Rational(numerator2, denominator2)
            return (rational1, rational2)
        except:
            return(Rational(0,0), Rational(0,0)) #if an entry value is missing, cause NaN

    def getBothImaginary(self):
        """ Helper method used by addComplex, subtractComplex, multiplyComplex and divideComplex methods"""
        try: 
            real1 = eval(self.complex1Real.get())
            imag1 = eval(self.complex1Imag.get())
            number1 = Imaginary(real1, imag1)
        except:
            return(Imaginary(0,0), Imaginary(0,0))
            
if __name__ == "__main__": GUI() 