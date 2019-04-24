a=input("Enter your unit : ")
if a<=150:
 b=a*2.40
 print "Bill : ",b
elif a>150 and a<=300:
 b=(a-150)*3.00+150*2.40
 print "Bill : ",b
else:
 b=(a-300)*3.20+150*2.40+150*3.00
 print("Bill :" ),b