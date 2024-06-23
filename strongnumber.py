i=145
temp=i
c=[]
while(temp>0):
    k=temp%10
    temp=temp//10
    fact=1
    sum=0 
   
    while (k>0):
        fact=fact*k
        k=k-1
    c.append(fact)
    print(fact)
print(c)
sum=0
for k in c:
    sum=sum+k
print(sum)

if(sum==i):
    print("Strong number")
else:
    print("Not a Strong number")
    
    
