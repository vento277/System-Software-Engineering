'''
Unified Modelling Lanuage is a modelling language. It helps with the communication 
for the design and visualizing the software system. 

They are usually drawin in boxes. And can show visibility as well. 

ClassName
Field
Methods

BMI
    __weight: float 
    __height: float
        __init__(weight: float, height: float)
        getBMI():float
        getStatus(): str
        
Student
    name: str
    studentNumber: int
    yearLevel: int = 1
        entroll(course: str): bool
        setYear(year: int = 2022): int
        
Name of an object is underlined.

The model above is a static view of the class. There are two diagrams to do this.

'Use case' diagram uses stick figure to represent the external actors involoved.
Medical receptionst - trasnfer data - Patient record system

'Seqeuntial diagram' shows the time sequency of the class's operation at the object level. 

We can also show relationship between classes using arrows. 
Inheritance (is a): ->
Association (verb in between ex. person rents a house): -

Student (5..60) -takes- (*) Course 
A student may take any number of course; and a course may have from five to sixty students.
* means an unlimited number, and n..m indicates that the number of objects is between m and n (inclusive).

Course (0..2) -teach- (1) Faculty
A faculty member may teach at most two course; and a course is taught by one faculty member.

Student (5..60) -takes- (*) Course (0..2) -teach- (1) Faculty

Aggregation (has a): -hollow diamond (-D) ex. house and family
Composition (if owning object is destoryed, so is the contained): -filled diamond (-D*) ex. dog and the tail

Name (1) -D* (1) Student (1) D- (1) Address

https://iastate.pressbooks.pub/workshopdemo/chapter/uml-class/
'''