class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def show_person(self):
		print("name :",self.name)
		print("age :",self.age)
#child class		
class student(person):
	def __init__(self,name,age,roll,branch):
		super().__init__(name,age,roll)
		self.branch=branch
	def show_engg(self):
	    print("branch :",self.branch)
e=enggstudent("Rahul",20,101,"computer science")
#calling method
e.show_person()
e.show_student()
e.show_engg()