a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
c=int(input("Enter the number3:"))
print("The second largest number is:")
if(a<b) & (a>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)