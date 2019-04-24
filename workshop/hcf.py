def computeHCF(x, y):
   while(y):
       x, y = y, x % y
   return x
a=int(input("enter first number : "))   
b=int(input("enter second number : "))
print(computeHCF(a, b))