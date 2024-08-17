decimal=int(input("enter your number : "))
d=str(decimal)
space=""
binary=""
while (decimal!=0):
    remainder = decimal%2
    binary = str(remainder)+space+binary
    decimal = decimal//2
print(binary)
