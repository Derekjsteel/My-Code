#!/usr/bin/python3
spec_char = ["@","$","%","^","&","_","-",".",",","?","!"]
ban_char = ["/","\\","|","{","}","<",">","#","*","\"","\'","[","]"," ",":",";","~","`"]
bc_print=""
for c in ban_char:
    bc_print += c
while True:
    g2g = True
    pw = input("Please enter your password: ")
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
    if any(ban in ban_char for ban in pw):
        print("Passwords cannot contain any of the following characters: \n" + bc_print)
        g2g = False
    if g2g == True:
        break
    else:
        continue
print("Your password is valid.")


