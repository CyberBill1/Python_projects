#1/bin/python3
username = input("Enter Username")
if username == "": #if the user didn't input any thing
    print("You did not input anything ")
else:
  print("Wrong, try again")
  
pin = input("Enter PIN")
if pin == "1234": #the correct pin here is "1234"
    print("Access granted")
else:
  print("wrong pin")