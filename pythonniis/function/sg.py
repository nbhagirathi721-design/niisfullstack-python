class student:
	def __init__(self,n,r,m):
		self.__name=n 
		self.__roll=r 
		self.__mark=m 
	def show(self):
		print("my name=",self.__name)
		print("my roll=",self.__roll)
		print("my mark=",self.__mark)
	def update():
		self.__name=n 
		self.__roll=r 
		self.__mark=m
	def set_name(self,name):
		self.__name=name
	def set_roll(self,roll):
		self.__roll=r
	def set_mark(self,mark):
		self.__mark=m
	def get_name(self):
	    return self.__name
	def get_roll(self):
	    return self.__roll
	def get_mark(self):
	    return self.__mark
s= student("muna",1,90.50)
s.show()
s.update("muna das",2,80.50)
s.show()

		 
		

		
