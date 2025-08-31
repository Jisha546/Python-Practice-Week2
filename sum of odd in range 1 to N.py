num=int(input("enter a number"))
for i in range(2,num):
    if num>0:
        if num%i==0:
            print(" not prime")
            break
        else:
            print(" prime")
    else:
     print("not prime")
