import re

emailAddress = input("Enter email addresses: ")

pat2 = "(\w+)@((\w+\.)+(com))"

if re.match(pat2, emailAddress):
    print("Valid")
else:
    print("Invalid")