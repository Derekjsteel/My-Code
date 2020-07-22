#!/usr/bin/python3
alph = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"
spec_char = "!@$%^&*()_-,.?"
allowed = list(alph.upper() + alph.lower() + nums + spec_char)
ac_print = ""
for ac in allowed:
    ac_print+=ac
while True:
    g2g = True
    pw = input("Please enter your password: ")
    if any(c not in allowed for c in pw):
        print("Invalid character. Allowed characters are: \n" + str(ac_print))
        g2g = False
    if len(pw)<10:
        print("Password must be at least 10 characters long.")
        g2g = False
    if not any(c.isupper() for c in pw):
        print("Password must have at least one uppercase letter.")
        g2g = False
    if not any(c.islower() for c in pw):
        print("Password must have at least one lowercase letter.")
        g2g = False
    if not any(c.isdigit() for c in pw):
        print("Password must have at least one number.")
        g2g = False
    if not any(special in spec_char for special in pw):
        print("Password must have at least one special character.")
        g2g = False
    if g2g == True:
        break
    else:
        continue
print("Your password is valid.")


