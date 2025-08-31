choice=("convert (c)elsius to (f)ahrenheit")
temp=float(input("enter the temperature"))
if choice=='c':
    print("temperature in celsius",(temp-32)*5/9)
else:
    print("temperature in fahrenheit",(temp*9/5)+32)