li=[]
f=0

n=int(input("Enter the number of input:"))
for i in range (1,n+1):
    b = int(input("Enter the elements:"))

    li.append(b)


for i in li:
    
    if i%2!=0:
        if f==0:
            s=i
            f=f+1
        else:
            if s>i:
                s=i
print(s)
