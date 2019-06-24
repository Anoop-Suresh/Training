class circle:
    def __init__(self,radius):
        self.radius=radius;

    def area(self):
        return self.radius*self.radius*3.14
r=int(input("Enter the Area:"))
c1=circle(r)
print(c1.area())