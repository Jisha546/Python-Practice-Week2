year=int(input("enter a year"))
if year%4==0 and year%100!=1:
    print("leap year")
else:
    print("not leap year")