import re

pat = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"

n = input("Press 1 for exit or Email address: ")

while(n!="1"):
    if re.match(pat,n):
        print("Valid Email")
    else:
        print("Invalid Email")
    n = input("Press 1 for exit or Email address: ")

