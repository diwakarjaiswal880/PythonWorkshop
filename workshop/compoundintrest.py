def compound_interest(p, r, t):  
    ci = p * (pow((1 + r / 100), t)) 
    print("Compound interest is", ci) 
p=float(input("Enter principle : "))
r=float(input("Enter rate : "))
t=float(input("Enter time : "))
compound_interest(p, r, t) 