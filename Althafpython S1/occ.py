txt=input("enter the text")
b=txt.split()
c=set(b)
for i in b:
    print(i,"=",b.count(i))
