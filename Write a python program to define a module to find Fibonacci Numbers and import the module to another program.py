import fibonacci_module
try:
	n=int(input("Enter the max value: "))
	if n>0:
		seq=fibonacci_module.fibbo_seq(n)
		print("Fibonacci series upto",n,":")
		for num in seq:
			print(num,end=' ')
	else:
		print("Please enter a positive integer")
except ValueError:
	print("Invalid input")
#write your code here
def fibbo_seq(max):
	seq =[]
	a,b=0,1
	for _ in range(max):
		seq.append(a)
		a,b=b,a+b
	return seq
