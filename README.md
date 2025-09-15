OVERVIEW 

The Arithmetic formatter is a Python function that formats arithmetic problems vertically. It  simulates  the way primary school students learn to solve addition and subtraction problems. This project was completed as part of the FreeCodeCamp Scientific Computing with Python certification.It represents  my first  complete program after working on a  series of mini-python projects also by freecode camp and a few  self pioneered projects.It also marks the  transition point where I moved from tracking code in  physical notebooks and scattered documents into the version control system.

PROJECT'S PURPOSE 

The core purpose of this project was to create a function that takes a list of simple arithmetic problems and returns the output  formatted in a vertical, columnar layout together with their solutions. This presentation makes it significantly easier to perform manual calculations, which is a fundamental skill taught in early education to younger students.

HOW IT WORKS 

The main function is :
```python
arithmetic_formatter(problems, show_answers=False)
```
1)problems(a list of strings mainly numbers and their operators)
2)show_answers(bool):If set to True, the formatted output will include the answers.else only the fomatted form will appear with no answer displayed  
 The Arithmetic Formatter allows users to enter arithmetic problems interactively. For instance ,when the program runs, you will be  first prompted to enter how many problems you intend to input. The program then asks for each problem one by one. These problems are collected into a list and passed to the main function:  



EXAMPLE FLOW 
```python
How many problems would you like to enter? 2  
Enter problem 1: 32 + 698  
Enter problem 2: 3801 - 2  

   32      3801
+ 698    -    2
-----    ------
  730      3799
```

KEY CONSTRAINTS

-Maximum problems(5): The function will only accept up to five problems at once.

-Max length of problem(3) : Only two numbers and a single operator 

-Operators: Only  handles addition (+) and subtraction (-) are supported. 

-Multiplication or division is not allowed.

-Operands: Each operand must consist of digits only (no letters, decimals, or special characters).

-Operand length: Each number may contain a maximum of four digits.

-Formatting: Problems are arranged vertically and aligned properly, with a line of dashes under each operator.

-Optional answers: Solutions are only displayed if show_answers=True.


RUNNING THE PROJECT 

OPTION 1

1)Clone this repository 
```bash
git clone https://github.com/keden49/arithmetic-formatter_project.git
```
2) Navigate into the project folder:
   ```bash
   cd arithmetic_formatter_project
   ```
3) Run the Python file:
   ```bash
   python arithmetic_formatter_draft.py
   ```
 4)4. Follow the prompts in your terminal.  
   Example:
   ```bash
   How many problems would you like to enter? 2
   Enter problem 1: 32 + 698
   Enter problem 2: 3801 - 2

      32      3801
   + 698    -    2
   -----    ------
     730      3799
   ```  
OPTION 2
import as a module 
```python
from arithmetic_formatter_draft import arithmetic_formatter
```

TAKEAWAY 

Completing this project gave me confidence in my coding journey. It proved I can move beyond small practice problems and build something structured, useful, and worth sharing.





