# 0. Write a boolean function that takes a non-negative integer as a parameter and returns True if the number is even, False if it is odd. It is common to call functions like this is_even.
def is_even(int):
	'''Returns true if number is even, false if odd'''
	divisibleByTwo = int % 2
	return divisibleByTwo == 0

# 1. Write a function that takes a non-negative integer as a parameter and returns the number of digits in it.
def amount_digits(num):
	'''Tells the amount of digits in a number'''
	num = str(num)
	length = len(num)
	return length
	
# 2. Write a function that takes a non-negative integer as a parameter and returns the sum of its digits.
def sum_digits(num):
	'''Returns the sum of every digit in a number added together'''
	sum = 0
	for digit in str(num):
		sum += int(digit)
	return sum
	
# 3. Write a function that takes a non-negative integer as a parameter and returns the sum of all the integers that are less than the given number.
def sum_less_ints(numbr):
	'''Returns the sum of every value in a number lower than itself'''
	sum = 0
	num = numbr - 1
	while num != 0:
		sum += num
		num -= 1
	return sum	
			
# 4. Write a function that takes a non-negative integer as a parameter and returns its factorial.
def factorial(num):
	'''Returns the factorial of num which is all its factors multiplied'''
	product = num
	if num != 0:
		while num != 1:
			product = product * (num - 1)
			num -= 1
	elif num == 0:
		product = 0
	return product
# 5. Write a boolean function that takes two positive integers as parameters and returns true if the second number is a factor of the first
def is_factor(x, y):
	'''Returns true if y is a factor of x'''
	seeIfFactor = x % y
	return seeIfFactor == 0
		
# 6. Write a boolean function that takes an integer greater than or equal to 2 as a parameter and returns whether the number is a prime.
def is_prime(int):
	'''Returns true if int is prime'''
	numbersToTry = range(2,(int))
	indicator = 0
	for number in numbersToTry:
		seeIfDivisible = int % number
		if seeIfDivisible == 0:
			indicator += 1
	return indicator == 0
	
# 7. Write a boolean function that takes a positive integer as a parameter and returns whether the number is perfect.
def is_perfect(int):
	'''returns true if number is perfect'''
	numbersBelow = range(1,int)
	sumFactors = 0
	properFactors = []
	for number in numbersBelow:
		if (int % number) == 0:
			properFactors.append(number)
	for number in properFactors:
		sumFactors += number
	return sumFactors == int
	
# 8. Write a boolean function that takes a positive integer as a parameter and returns true if the sum of the digits of the number divides evenly into the number, false otherwise.
def divides_evenly(int):
	'''returns true if sum of the digits of a number divides evenly into the number itself'''
	sumOfDigits = sum_digits(int)
	return (int % sumOfDigits == 0)
	
		
	
	
	
	
	
	
	
	
	
	