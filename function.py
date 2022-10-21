#!/bin/python3
def add(name):
    print("Welcome "+ name +", Good morning")
    print("Thanks for coming")

add("dennis")

def add2(num1, num2, num3):
    print(num1 + num2 + num3)

add2(2, 2, 2)
    #OR
def add3(num1, num2, num3):
    result = num1 + num2 + num3
    print(result)

add3(2, 2, 2)

def highestNumber(input1, input2):
  if input1 > input2:
    print("highest number is "+ str(input1))
  else:
    print("highest number is "+ str(input2))


highestNumber(80, 50)
            #OR
def highestNumber(input1, input2):
  if input1 > input2:
    print("highest number is", input1)
  else:
    print("highest number is", input2)


highestNumber(80, 50)