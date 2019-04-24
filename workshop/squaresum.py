def squaresum(n) : 
    sm = 0
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
      
    return sm  
n = int(input("Enter a number to find squaresum : "))
print(squaresum(n)) 