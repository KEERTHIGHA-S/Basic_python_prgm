class demo:
    def __init__(self,value=None):
        self.value=value
        
    def display(self,i):
        
        while(i<5):
            print(i)
            i=i+1
        print("end")
        
d=demo()
d.display(1)
        
