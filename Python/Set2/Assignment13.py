import re

n=input("Enter a string:")

al=re.findall('[0-9]{10}',n )
print(al)

