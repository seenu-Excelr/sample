d=input("Enter some text into the file:")
i=input("Enter the file name:")
c=0
r=1
l=len(d)
f=open(i,'w')
f.write(d)
f.seek(0)
while(r<=l):
    if f.read(r)==" ":
        c+=1
    r+=1
print("total no.of words:",c)
