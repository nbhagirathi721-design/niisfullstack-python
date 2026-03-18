from abc import *
class shape(ABC):
    def __init__(self,name):
    	self.name=name
    @abstractmethod
    def perimeter(self):
        pass
class rectangle(shape):
    def __init__(self,n,L,B):
       super().__init__(n)
       self.L=L 
       self.B=B 
    def perimeter(self):
        return 2*(self.L+self.B) 

class square(shape):
    def __init__(self,n,L):
       super().__init__(n)
       self.L=L 
    def perimeter(self):
        return 4*self.L 
r1=rectangle("rect",5,7)
print(r1.area)
s1=square("sq",7)
print(s1.area)
