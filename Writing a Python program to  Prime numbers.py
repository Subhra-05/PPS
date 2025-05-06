def is_prime(num):
	if num<2:
		return False
	for i in range(2,num):
		if num%i==0:
			return False
	return True
upper_limit = int(input("Enter upper limit: "))
for i in range (2,upper_limit):
	if is_prime(i):
		print(i)
