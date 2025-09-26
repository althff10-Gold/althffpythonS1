x=1
while(x == 1):
    print("MENU")
    print("1. find occurance of word")
    print("2. find character frequency")
    print("3. display the factors of a given number")
    print("4. exit")

    z = int(input("\nchoose one of the option from menu(1-4)"))
    if z == 1:
        a = input("enter the text :")
        b = a.split()
        s = set(b)
        for i in s:
            print(i,"=",b.count(i))
    elif z == 2:
         a = input("enter the text:")
         b = set(a)
         for i in b:
             print(f"{i} = {a.count(i)}")
    elif z == 3:
         a = int(input("enter a number :"))
         for i in range(1, a+1):
             if a % i == 0:
                 print(i)
 
    elif z == 4:
         x+=1
    else:
        print("\ninvalid input")
