usrnm=input("enter the name: ")

if ((len(usrnm)>12) or not(usrnm.isalpha())):
    print("Invalid username")
else: 
    print("Valid username")