class votererror(baseexception):
	def __init__(self,name):
		super().__init__()
print("enter a age")
age=input
if age>=18:
	print ("eligbal")
else:
	try:
		raise voter error ("age not allow")
	except:
	    print("not allow")
print("main end")

