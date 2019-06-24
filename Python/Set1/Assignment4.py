n=input("Enter the strings seperated by commas:")

words=sorted(n.split(','))
newsorted=','.join(words)
print(newsorted)