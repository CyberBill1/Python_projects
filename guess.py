
#from ast import While


name = "Dennis"

userguess = ""
while name != userguess:
   username = input("Enter your username")
   if username == name:
        print("Acces granted")
   else:
        print("Wrong, try again")