num=int(input("enter a number"))
a,b=0,1
print("fibonacci series:")
for i in range(num):
    print(a,end=" ")
    a,b=b,b+a