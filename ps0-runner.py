import ps0

# 0. Write a boolean function that takes a non-negative integer as a parameter and returns True if the number is even, False if it is odd. It is common to call functions like this is_even.
print("0 is even: {}".format(ps0.is_even(0)))
print("14 is even: {}".format(ps0.is_even(14)))
print("907 is even: {}".format(ps0.is_even(907)))

#1. Returns how many digits a number has
print("0 has {} digits".format(ps0.amount_digits(0)))
print("3 has {} digits".format(ps0.amount_digits(3)))
print("10 has {} digits".format(ps0.amount_digits(10)))
print("5678 has {} digits".format(ps0.amount_digits(5678)))

#2.  Write a function that takes a non-negative integer as a parameter and returns the sum of its digits.
print("the sum of the digits in 0 is {}".format(ps0.sum_digits(0)))
print("the sum of the digits in 34 is {}".format(ps0.sum_digits(34)))
print("the sum of the digits in 112 is {}".format(ps0.sum_digits(112)))

#3. Write a function that takes a non-negative integer as a parameter and returns the sum of all the integers that are less than the given number.
print("The sum of integers lower than 1 is {}".format(ps0.sum_less_ints(1)))
print("The sum of integers lower than 5 is {}".format(ps0.sum_less_ints(5)))

# 4. Write a function that takes a non-negative integer as a parameter and returns its factorial.
print("The factorial of 0 is {}".format(ps0.factorial(0)))
print("The factorial of 5 is {}".format(ps0.factorial(5)))

#5. Write a boolean function that takes two positive integers as parameters and returns true if the second number is a factor of the first
print("10 is a factor of 20: {}".format(ps0.is_factor(20,10)))
print("7 is a factor of 30: {}".format(ps0.is_factor(30,7)))
print("300 is a factor of 50: {}".format(ps0.is_factor(50,300)))

#6. Write a boolean function that takes an integer greater than or equal to 2 as a parameter and returns whether the number is a prime.
print("2 is prime: {}".format(ps0.is_prime(2)))
print("7 is prime: {}".format(ps0.is_prime(7)))
print("13 is prime: {}".format(ps0.is_prime(13)))
print("20 is prime: {}".format(ps0.is_prime(20)))

# 7. Write a boolean function that takes a positive integer as a parameter and returns whether the number is perfect.
print("1 is a perfect number: {}".format(ps0.is_perfect(1)))
print("6 is a perfect number: {}".format(ps0.is_perfect(6)))
print("15 is a perfect number: {}".format(ps0.is_perfect(15)))
print("496 is a perfect number: {}".format(ps0.is_perfect(496)))

# 8. Write a boolean function that takes a positive integer as a parameter and returns true if the sum of the digits of the number divides evenly into the number, false otherwise.
print("The sum of the digits in 20 divides evenly into 20: {}.".format(ps0.divides_evenly(20)))
print("The sum of the digits in 34 divides evenly into 34: {}.".format(ps0.divides_evenly(34)))
print("The sum of the digits in 315 divides evenly into 315: {}.".format(ps0.divides_evenly(315)))