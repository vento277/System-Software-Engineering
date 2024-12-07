'''
A development life-cycle is a clearly defined steps of which the developers follow to produce a software. There are a few models of them:
Code and fix - write first and fix as one goes.
    Good for small projects and can progress quickly. But is not suitable to produce good quality codes
Waterfall - Perform each step in order.
    Good for projects that are large and well understood (efficienct if something dosen't need to go back). But it is not suitable for making changes as all the planning are done and to be followed. Not adaptable. No sense of progress.
    It is usually used for extremely delicate products such as Mars Rovers and such. 
Agile - Divide the project into much smaller tasks and do them incrementally with iteration.
    Good for smaller teams to tackle problems quickly and release early (early feedback). But it requires the product to be decomposable and there may be times where earily 'sprints' are re-wored in the later ones. 

These are the general steps of software dev:
Feasibility - Go or no go decisions
Requirement - Description of the serivce under the provided constraint
System and Porgram design - Developer's view on the solution
Implmentation - Coding
Acceptance and Release - Testing the system aginst the contraint
Maintainence - Changing the system to better fit the need

Testing the software is an important part of producing a good quality software. 

Validation is a process to check if the software is working accoridng to the specifications. It includes testing, code review and formal reasoning.
    Code review is a systemetic study of the source code to ensure correctness.
    
Software testing is hard beacuse exhaustive (can't cover all cases) testing is infeasible and haphazard (try and see if ti works) testing is unreliable. 
This is why we use test suits. They are collection of test cases that increases the likelihood to find a bug.

Blackbox testing chooses only the test cases from the spec. This is called a blackbox since we don't know the implementation. 
Whitebox testing chooses test cases with the knowledge of the implementation. 

Testing should be done contrctutively, in stages. 
Unit testing is testing the codes indivisually on its own methods or objects.
Integration testing is testing the code as a group
Acceptance testing is testing the code to see if it fullfills the user's requirements. 
'''
import unittest

class Arithmetic:
    def add(a: float, b: float) -> float:
        return a + b

    def subtract(a: float, b: float) -> float:
        return a - b

class Test(unittest.TestCase):
    def test_add(self):
        a, b = 2, 13
        self.assertEqual(Arithmetic.add(a, b), a + b)
        
    def test_subtract(self):
        a, b = 123, 11
        self.assertEqual(Arithmetic.subtract(a, b), a - b)

if __name__ == "__main__":
    
    arithmetic = Arithmetic()
    
    # Using assert keyword
    a, b = 1, 12
    assert a + b == Arithmetic.add(a, b) # Python keyword. Raise assertion error if the expression is False.
    
    # Using the unittest module
    unittest.main()