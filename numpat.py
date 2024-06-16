class numpat:
    def __init__(self, value=None):
        self.value = value

    def display(self, i):
        if i > 9:
            return
        if i % 3 == 1:
            print("\n")
        print(i)
        self.display(i + 1)

# Create an instance of numpat and call the display method
p1 = numpat()
p1.display(1)
