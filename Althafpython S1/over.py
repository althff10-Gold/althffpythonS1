num=input("enter the numbers")
a=num.split()
for i in a:
    i=int(i)
    if (i>100):
        print("over")
    else:
        print(i)
