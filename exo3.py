x=input("enter the total amount recieved :  ")
x=int(x)
if (x<=1000000):
    tax=(x*5)/100
    print ("your tax to pay is : " +str(tax))
else: tax =(x*15)/100
print ("your tax to pay is :  " + str(tax))