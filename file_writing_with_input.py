#!/usr/bin/python3

import sys

while True:
    while True:
        fn = input("What is your first name? ")
        if fn.isalpha():
            break
        else:
            print("Please only use letters in your name.")
            continue

    while True:
        ln = input("What is your last name? ")
        if ln.isalpha():
            break
        else:
            print("Please only use letters in your name.")
            continue

    while True:
        adr = input("What is your address ")
        if all(l.isalnum() or l.isspace() for l in adr):
            break
        else:
            print("Please only use letters and numbers in your address.")
            continue

    if fn.isalpha() and ln.isalpha() and all(l.isalnum() or l.isspace() for l in adr):
        print("Welcome to the concrete jungle, " + fn.title() + " " + ln.title() + "!")

    with open("employees.txt", "a") as file:
        file.write((ln.title() + ", " + fn.title() + "\n" + adr.title() + "\n\n"))

    y = input("Would you like to add another? (Y/n) ")
    try:
        if (y.lower()=="y") or (y==""):
            continue
        else:
            sys.exit()
    except:
        break
        print("Unexpected error")