from abc import *
class shape(ABC):
    def __init__(self,name):
    	self.name=name
    @abstractmethod
    def perimeter(self):
        pass
class rectangle(shape):
    def __init__(self,n,l,b):
       super().__init__(n)
       self.l=l 
       self.b=b 
    def perimeter(self):
        return 2*(self.l+self.b) 

class square(shape):
    def __init__(self,n,l):
       super().__init__(n)
       self.l=l 
    def perimeter(self):
        return 4*self.l 
r1=rectangle("rect",5,7)
print(r1.perimeter())
s1=square("sq",7)
print(s1.perimeter())
