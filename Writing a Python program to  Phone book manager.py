# write your code...
phone_book={}
while True:
	print("1. Add Contact")
	print("2. Remove Contact")
	print("3. Display")
	print("4. Quit")

	choice=input("Enter choice (1-4): ")
	if choice =='1':
		name=input("Name: ")
		phone_number=input("Phone number: ")
		phone_book[name]=phone_number
	elif choice=='2':
		name=input("Name: ")
		if name in phone_book:
			del phone_book[name]
		else:
			print("Not found")
	elif choice=='3':
		print(phone_book)
	elif choice=='4':
		break
	else:
		print("Invalid")
