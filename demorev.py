class demorev:
    def __init__(self,value=None):
        self.value=value
        
    def display(self,i):
        
        while(i<6):
            print(i)
            if(i==0):
                break
            i=i-1
        print("end")
        
d=demo()
d.display(5)
        
