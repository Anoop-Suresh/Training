f=open("/home/anoop/PycharmProjects/Assignments/Set1/Assignment9.txt","r")
linecount=0
wordscount=0
charcount=0

for i in f :

    linecount=linecount+1
    words=i.split()
    wordscount=wordscount+len(words)
    charcount = charcount + (len(i) - ((linecount-1)*1))


print("Nuber of lines is",linecount)
print("Word count is ",wordscount)
print("Number of Character",charcount)
