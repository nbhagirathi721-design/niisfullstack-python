class square:
    def __init__(self,a):
        self.arm=a
    def show(self):
        print("arm=",self.arm)
    def area(self):
        return self.arm*self.arm
    def perimeter(self):
        return 4*self.arm
s1=square(10)
s1.show()
print("area of square=",s1.area())
s1.perimeter()
print("perimeter of square=",s1.perimeter())
                     