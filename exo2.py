x=input("enter the bill of internet")
y=input("enter the electricity bill")
z=input("enter the water bill")
x=int(x)
y=int(y)
z=int(z)
bill=x+y+z
if ((bill/3)>=12000):
    discount= (bill*10)/100
    bill_new=bill-discount
    print("you have to pay the new bill :" +str(bill_new))
else:
    print ("you have to pay : " +str(bill))