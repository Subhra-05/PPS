digit1=int(input("digit1 (0-9): "))
digit2=int(input("digit2 (0-9): "))
digit3=int(input("digit3 (0-9): "))
if(0<=digit1<=9 and 0<=digit2<=9 and 0<=digit3<=9):
	digits=[digit1,digit2,digit3]
	print(f"{digits[0]}{digits[1]}{digits[2]}")
	print(f"{digits[0]}{digits[2]}{digits[1]}")
	print(f"{digits[1]}{digits[0]}{digits[2]}")
	print(f"{digits[1]}{digits[2]}{digits[0]}")
	print(f"{digits[2]}{digits[0]}{digits[1]}")
	print(f"{digits[2]}{digits[1]}{digits[0]}")
else:
	print("Invalid")
