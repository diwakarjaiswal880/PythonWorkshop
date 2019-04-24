n=int(input("Enter a number to check prime or not : "))
if(n>1):
	for i in range (2,n//2):
		if(n%i==0):
			print("Number is not prime")
			break
	else:
		print("Number is prime")
else:
	print("Number is not prime")			