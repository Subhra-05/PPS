a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a>b and a>c:
	print(f'Largest number: {a}')
elif b>a and b>c:
	print(f'Largest number: {b}')
else:
	print(f'Largest number: {c}')
