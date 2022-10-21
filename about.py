#!/bin/python3
print("Hello, World!")
print()  # or "print('\n')" to give a new line
print("How are you")

firstname = "Obumuneme"
middlename = 'Dennis'
lastname = "Offordile"
fullname = firstname+ " " +middlename + " " +lastname

age = 17 # This is an integer because it doesn't have a quote i.e ""
height = 5.2 # This is a float because it has a decimal and doesn't have a quote
birthday = 1 # This is an integer

print(age)
print(int(height)) # To print height without a decimal
print(fullname)

print(firstname,middlename,lastname) # It gives space automatically
print(firstname+ " " +middlename + " " +lastname) # To give space
print("My name is ", firstname , middlename , lastname ," and I am "+ str(age)+" years old, with a height of "+ str(height))
print(type(age)) # To print the class age falls under
print(type(height)) # To print the class height falls under

print(fullname.upper()) # To print all in capital letters
print(fullname.lower()) # To print all in small letters
print(fullname.title()) # To print all the first letters
print(fullname.capitalize()) # To print only the first letter in the sentence as a capital letter.
print(len(fullname)) #to count the number of alhpabets in the sentence including the space .

