i=int(input("Enter the number of fibonacciseries"))
fn=int(input("Enter the first number"))
sn=int(input("Enter the second number"))
while(i>=0):
    c=fn+sn
    fn=sn
    sn=c
    i=i-1
    print(c)
    