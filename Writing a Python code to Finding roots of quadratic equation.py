import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d =(b**2) - 4*(a*c)
if d>0:
	r1=(-b + math.sqrt(d))/(2*a)
	r2=(-b - math.sqrt(d))/(2*a)
	print(f"The roots are: {r1:.2f} and {r2:.2f}")
elif d==0:
	root = -b/(2*a)
	print(f"The root is: {root:.2f}")
else:
	real = b/(2*a)
	img = math.sqrt(abs(d))/(2*a)
	print(f"The roots are: {-real:.2f}+{img:.2f}j and {-real:.2f}-{img:.2f}j")
