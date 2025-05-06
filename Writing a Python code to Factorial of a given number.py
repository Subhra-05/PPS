def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)


try:
	num = int(input("Enter a number : "))
	if num < 0:
		print("Enter a positive number")
	else:
		print(f"Factorial of given number is : {factorial(num)}")
except ValueError:
	print("Invalid input. PLease enter a number.")
