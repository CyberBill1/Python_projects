#!/bin/python3
# converting str to int that is what "int" is doing before the "(input("question"))"
score = int(input("What is your score")) 

if score >= 90 :
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
elif score >= 40:
    print("E")
elif score >= 30:
    print("F9")
else:
    print("You will have to rewrite this exam")