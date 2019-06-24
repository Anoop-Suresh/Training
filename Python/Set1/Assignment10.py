lst=["Anoop","Sanoop","Girija","Suresh"]

if (len(lst)==0):
    print("Nobody likes this")
if (len(lst)==1):
    print(lst[0] +"likes this")
if(len(lst)==2):
    print(lst[0]+" and "+lst[1]+" likes this ")
if (len(lst)==3):
    print(lst[0]+","+lst[1]+" and "+lst[2]+" likes this")
if(len(lst)>3):
    l=len(lst)-2
    print(lst[0]+","+lst[1]+" and "+str(l)+" others likes this")