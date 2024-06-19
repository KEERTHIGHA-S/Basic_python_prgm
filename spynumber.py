i=int(input("Enter the number:"))
pro=1
sum=0
while(i>0):
    c=i%10
    pro=pro*c
    i=i//10
    sum=sum+c
print("The product:", pro)
print("The sum:", sum)
if(sum==pro):
    print("spy number")
else:
    print("Not a spy number")
    