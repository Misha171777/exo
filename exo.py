def authorised(age,gender):
    if age<=18:
        if gender!="male":
            reponse="authorise au service militaire"
        else:
            reponse="non authorise"
        return reponse
name=input("enter your name  ")
age=int(input("enter your age  "))
gender=input("enter your gender  ")
print("your name is: "+ name + " and you're"+authorised (age,gender))
