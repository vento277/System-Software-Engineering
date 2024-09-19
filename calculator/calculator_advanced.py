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
    def __init__(self, flag, numerator: int, denominator: int) -> None:
        """initizer stores the rational number in the lowest form.
           A flag has been added to process negatives and inputs for the 
           imaginary number calculation.
        """ 
        def greatestCommonDivisor(n: int, d: int):
            if flag == 1:
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
            else:
                return 1
        #rational number must be in the lowest form 
        
        gcd: int = greatestCommonDivisor(numerator, denominator)
        self.flag = flag # Store the flag value

        if flag == 1:
            # If flag is 1, adjust the sign and reduce the rational number
            signFactor: int = 1 if denominator > 0 else -1 #numerator stores the sign of the rational
            self.numerator = signFactor * numerator // gcd
            self.denominator = abs(denominator) // gcd

        else:
            # If flag is not 1, store the numerator and denominator as is
            self.numerator = numerator 
            self.denominator = denominator 

    def add(self, secondRational):
        """adds 'this' rational to secondRational
           returns the result as a rational number (type Rational)
        """  
        # r1 = a/b r2 = c/d; r1 + r2 = [(a*d) + (b*c)] / (b*d) 
        numerator  = ((self.numerator * secondRational.denominator) + (self.denominator * secondRational.numerator))
        denominator = (self.denominator * secondRational.denominator)
        number = Rational(1, numerator, denominator) # return the result as type Rational
        return number
    
    def subtract(self, secondRational):
        """subtracts secondRational from 'this' rational to 
           returns the result as a rational number (type Rational)
        """ 
        # r1 = a/b r2 = c/d; r1 + r2 = [(a*d) - (b*c)] / (b*d) 
        numerator  = ((self.numerator * secondRational.denominator) - (self.denominator * secondRational.numerator))
        denominator = (self.denominator * secondRational.denominator)
        number = Rational(1, numerator, denominator) # return the result as type Rational
        return number

    def multiply(self, secondRational):
        """multiplies 'this' rational to secondRational
           returns the result as a rational number (type Rational)
        """ 
        # r1 = a/b r2 = c/d; r1 + r2 = (a*c) / (b*d) 
        numerator  = (self.numerator * secondRational.numerator)
        denominator = (self.denominator * secondRational.denominator)
        number = Rational(1, numerator, denominator) # return the result as type Rational
        return number

    def divide(self, secondRational):
        """divides 'this' rational by secondRational
           returns the result as a rational number (type Rational)
        """ 
        # r1 = a/b r2 = c/d; r1 + r2 = (a*d) / (b*c) 
        numerator  = (self.numerator * secondRational.denominator)
        denominator = (self.denominator * secondRational.numerator)
        number = Rational(1, numerator, denominator) # return the result as type Rational
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

    #---Replica functions from above have been added for the complex number operation---

    def addComplex(self, secondImaginary):
        """adds 'this' imaginary to secondImaginary
           returns the result as a imaginary number (type Rational).
           Additionally, round the result to 3 decimal places.
        """  
        # a = x+yi b = u+vi; (x+u) + (y+v)i
        real = round(self.numerator + secondImaginary.numerator,3)
        imag = round(self.denominator + secondImaginary.denominator,3)
        number = Rational(0, real, imag) # return the result as type Rational
        return number
    
    def substractComplex(self, secondImaginary):
        """subtracts secondImaginary from 'this' imaginary to 
           returns the result as a imaginary number (type Rational).
           Additionally, round the result to 3 decimal places.
        """ 
        # a = x-yi b = u-vi; (x+u) - (y+v)i
        real = round(self.numerator - secondImaginary.numerator,3)
        imag = round(self.denominator - secondImaginary.denominator,3)
        number = Rational(0, real, imag) # return the result as type Rational
        return number
    
    def multiplyComplex(self, secondImaginary):
        """multiplies 'this' imaginary to secondImaginary
           returns the result as a imaginary number (type Rational).
           Additionally, round the result to 3 decimal places.
        """ 
        # a = x-yi b = u-vi; (x*u-y*v) + (x*v+y*u)i
        real = round((self.numerator * secondImaginary.numerator) - (self.denominator * secondImaginary.denominator),3)
        imag = round((self.numerator * secondImaginary.denominator) + (self.denominator * secondImaginary.numerator),3)
        number = Rational(0, real, imag) # return the result as type Rational
        return number
    
    def divideComplex(self, secondImaginary):
        """divides 'this' imaginary by secondImaginary
           returns the result as a imaginary number (type Rational).
           Additionally, round the result to 3 decimal places.
        """ 
        # a = x-yi b = u-vi; ((x*u+y*v) / (u^2+v^2)) + ((y*u-x*v) / (u^2+v^2))i
        try: 
            real = round(((self.numerator * secondImaginary.numerator) + (self.denominator * secondImaginary.denominator)) / ((secondImaginary.numerator)**2 + (secondImaginary.denominator**2)),3)
            imag = round(((self.denominator * secondImaginary.numerator) - (self.numerator * secondImaginary.denominator)) / ((secondImaginary.numerator)**2 + (secondImaginary.denominator**2)),3)
            number = Rational(0, real, imag) # return the result as type Rational
        except ZeroDivisionError:
            real = 0
            imag = 0
            number = Rational(2, real, imag) # Return the result as type Rational, initializing the flag to 2 to handle NaN when division is not possible. For example, division is invalid when b is 0.
            
        return number
    
    def toStringComplex(self):
        """ returns a string representation of 'this' imaginary
            the format is: (numerator)+(denominator)*i in float type with at most 3 decimal place. 
            if 'this' imaginary is absent of either the real or imaginary part, it should only show where the number exists. For example,
            if the result is 1i, it should not show 0+1i, instead show 1i only. 
        """ 
        # Flag will be raised(2) when:
        #   - the denominator of the imaginary division operation is 0
        #   - the input is not a number or is empty
        # which then the calculator will return "NaN" 
        if self.flag == 2:
            return 'NaN'
        elif self.numerator == 0 and self.denominator == 0:
            return '0.0' # Return 0 as a float if the result is 0. 
        elif self.numerator == 0:
            return str(float(self.denominator)) + 'i' # Return only the imaginary part if there is no real part in the result. 
        elif self.denominator == 0:
            return str(float(self.numerator)) # Return only the real part if there is no imaginary part in the result. 
        elif self.denominator < 0: 
            return str(float(self.numerator)) + str(float(self.denominator)) + 'i' # Return the negatives without the brackets, for example, 1-i or -1-i.
        return str(float(self.numerator)) + '+' + str(float(self.denominator)) + 'i' # Return the result in the format a+bi on all other cases. 

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

        
        #---Replica functions for GUI from above have been added for the complex number operation---
        # The GUI now has both the rational number calculator at the top and the imginary number calculator at the bottom.
        # The user will be able to use both, without one's result being affect by another. 

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

    #---Replica functions from above have been added for the complex number operation---
    # The flags are initiated at to ensure a proper input is entered. Input that is not a number (or empty) will raise the flag to 2, for which will return "NaN" 

    def addComplex(self):
        (imaginary1, imaginary2) = self.getBothImaginary()
        if imaginary1.flag == 2 or imaginary2.flag == 2:
            self.complexResult.set('NaN')
        else:
            complexResult = imaginary1.addComplex(imaginary2)
            self.complexResult.set(complexResult.toStringComplex())

    def subtractComplex(self):
        (imaginary1, imaginary2) = self.getBothImaginary()
        if imaginary1.flag == 2 or imaginary2.flag == 2:
            self.complexResult.set('NaN')
        else:
            complexResult = imaginary1.substractComplex(imaginary2)
            self.complexResult.set(complexResult.toStringComplex())

    def multiplyComplex(self):
        (imaginary1, imaginary2) = self.getBothImaginary()
        if imaginary1.flag == 2 or imaginary2.flag == 2:
            self.complexResult.set('NaN')
        else:
            complexResult = imaginary1.multiplyComplex(imaginary2)
            self.complexResult.set(complexResult.toStringComplex())

    def divideComplex(self):
        (imaginary1, imaginary2) = self.getBothImaginary()
        if imaginary1.flag == 2 or imaginary2.flag == 2:
            self.complexResult.set('NaN')
        else:
            complexResult = imaginary1.divideComplex(imaginary2)
            self.complexResult.set(complexResult.toStringComplex())

    def getBothRational(self):
        """ Helper method used by add, subtract, multiply and divide methods"""
        try:
            numerator1 = eval(self.rational1Numerator.get())
            denominator1 = eval(self.rational1Denominator.get())
            rational1 = Rational(1, numerator1, denominator1)

            numerator2 = eval(self.rational2Numerator.get())
            denominator2 = eval(self.rational2Denominator.get())
            rational2 = Rational(1, numerator2, denominator2)
            return (rational1, rational2)
        except:
            return(Rational(1,0,0), Rational(1,0,0)) #if an entry value is missing, cause NaN

    #---Replica functions from above have been added for the complex number operation---

    def getBothImaginary(self):
        """ Helper method used by addComplex, subtractComplex, multiplyComplex and divideComplex methods"""
        try: 
            real1 = eval(self.complex1Real.get())
            imag1 = eval(self.complex1Imag.get())
            imaginary1 = Rational(0, real1, imag1)

            real2 = eval(self.complex2Real.get())
            imag2 = eval(self.complex2Imag.get())
            imaginary2 = Rational(0, real2, imag2)
            return (imaginary1, imaginary2)
        except:
            return(Rational(2,0,0), Rational(2,0,0)) # if an entry is missing or invalid, raise the flag to 2. 
            
if __name__ == "__main__": GUI() 