txt=input("enter the names")
a=txt.split()
count=0
for i in a:
    for word in list(i):
        if "a" in word:
            

        
            count += 1
            print(count)
