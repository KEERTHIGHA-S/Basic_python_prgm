class revnum:
    def __init__(self,value=None):
        self.value=value
        
    def display(self,i):
        sum=0
        n=0
        while(i>0):
            n=i%10
            print(n)
            i=i//10
            sum=sum*10+n
        print(sum)    
    
re=revnum()
re.display(456)

print("end")
        
