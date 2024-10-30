# System-Software-Engineering
CPEN 333 is a 3rd year computer engineering course offered by the University of British Columbia.

*Course Description: Operating systems principles, real-time systems, principles of concurrent and multi-threaded programming, information structures, introduction to object oriented analysis, design, and modeling using UML, testing of software systems.*

## Tic-Tac-Toe
A command-line tic-tac-toe game where you can play against the computer. In the simple mode, the computer makes random moves, while in the advanced mode, it uses strategies that guarantee it never loses. For more information about the game, see Tic-tac-toe on Wikipedia (https://en.wikipedia.org/wiki/Tic-tac-toe), and for winning strategies, refer to WikiHow's guide (https://www.wikihow.com/Win-at-Tic-Tac-Toe).

## Rational Number Calculator
A rational number calculator with a graphical user interface (GUI) offers two main options. The basic calculator allows users to perform addition, subtraction, multiplication, and division of rational numbers, presenting results in their lowest terms. The advanced calculator provides additional functionality for calculations involving imaginary numbers (https://en.wikipedia.org/wiki/Complex_number), displaying results in floating-point format rounded to three decimal places.

## Sudoku Solution Validator
A solution validator for a sudoku puzzle (https://en.wikipedia.org/wiki/Sudoku) that uses a 9 x 9 grid in which each column, each row, as well as each of the nine 3 x 3 subgrids must contain all of the digits 1 to 9. The basic version operates with a single process, while the advanced version uses multiple processes (27 processes).

## List Sorter and File Download Speed Tester
A multithreaded sorting program that sorts a list of integers. Additionally, a program that compares the time taken to download a specified number of files from the Internet using two methods: sequentially (downloading one file after the other without threading) and through multithreading (assigning the download of each file to a separate thread).

# Dining-Philosopher's Problem
A multiprocessing implementation of the dining-philosophers synchronization problem. Note that in the provided code, we are using some random delay to simulate the time a philosopher takes to eat or to think. In total, there are three parts to the solution to avoid deadlock. They are: 
1. "Our program as usual will spawn five processes to represent the five philosophers, but we only allow four philosophers to be sitting at the dining table (so to speak) to eat at any given time to limit the number of philosophers at the table."
2. "Allow a philosopher to pick up her chopsticks only if both chopsticks are available."
3. "Use an asymmetric solution, e.g. an odd philosopher picks up first her left chopstick and then her right chopstick, whereas an even philosopher picks up her right first and then her left chopstick."
