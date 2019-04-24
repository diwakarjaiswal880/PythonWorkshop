def power(a, n): 
    if n==0: 
        return 1
    if n%2==0: 
        return power(a, n/2)*power(a, n/2) 
    return a*power(a, n/2)*power(a, n/2) 
def order(x):
    n=0
    while(x):
        n+=1
        x/=10
    return n        
def isArmstrong(x):
    n=order(x)
    temp=x
    s=0
    while(temp):
        a=temp%10
        temp/=10
        s=s+power(a,n)
    return(s)    
x = int(input("Enter a number to check armstrong or not : "))
m=isArmstrong(x)
if(m==x): 
    print(x," is an armstrong number.")
else:
    print(x," is not an armstrong number.")     