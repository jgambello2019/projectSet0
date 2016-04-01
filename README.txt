4/1
Author: Jack Gambello

Problem Set 0
About Problem Sets
A problem set is a series of classic problems in an introductory programming course. For these exercises, you must write your own functions from scratch. So you may not, for example, import a python function from another module, or use typecasting to make a problem trivial. You will have about a week to complete a problem set, and a small amount of class time to work on the project.



How to Submit

All functions should be written in one file called ps0.py . That file should not have a main program. In a separate file called ps0-runner.py write a simple main program that shows that each of your functions works by including several test cases. Remember you will have to import your ps0 file. Finally, all git repositories should have a README.txt and a .gitignore


The Problems
0. Write a boolean function that takes a non-negative integer as a parameter and returns True if the number is even, False if it is odd. It is common to call functions like this is_even.

1. Write a function that takes a non-negative integer as a parameter and returns the number of digits in it.

2. Write a function that takes a non-negative integer as a parameter and returns the sum of its digits.

3. Write a function that takes a non-negative integer as a parameter and returns the sum of all the integers that are less than the given number.
For example: sum_less_ints(3) → 3, which is 1 + 2
         sum_less_ints(5) → 10, which is 1 + 2 + 3 + 4


4. Write a function that takes a non-negative integer as a parameter and returns its factorial.
For example: factorial(3) → 6
     (because 6 = 3 * 2 * 1)
factorial(5) → 120
     (because 120 = 5 * 4 * 3 * 2 * 1)


5. Write a boolean function that takes two positive integers as parameters and figures out whether the second number is a factor the first. In other words, returns true if the second number divides into the first number evenly, and false otherwise.

6. Write a boolean function that takes an integer greater than or equal to 2 as a parameter and returns whether the number is a prime.

7. Write a boolean function that takes a positive integer as a parameter and returns whether the number is perfect. A perfect number is a number that equals the sum of proper its proper factors. A proper factor is any factor except the number itself.  
For example: isPerfect(6) → True
     (because 6 = 1 + 2 + 3)

8. Write a boolean function that takes a positive integer as a parameter and returns true if the sum of the digits of the number divides evenly into the number, false otherwise. You MUST call the sum_digits function you wrote in question 2 to define this function.