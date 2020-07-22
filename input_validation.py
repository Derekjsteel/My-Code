#!/usr/bin/python3
#Written by: Derek J. Steel
#June 24, 2020 at 20:15(MST)

#Basic while loop, used to continue asking for input until valid input is given.
while True:
    x=input("What is your number? ")#Ask for a value for x.
    try:# try this.
        x= int(x)#Is x an integer?
    except:#If it fails (throws an exception) do this.
        try:
            x= float(x)#Is x a float?
        except:#If x is neither an integer nor a float, print this and go back to the start.
            print("Your value could not be calculated. Please use a number.")
            continue#Continue the loop
    break#If either try works, break the loop.

#Printing your number to validate that it worked.
print("Your number is " + str(x))

