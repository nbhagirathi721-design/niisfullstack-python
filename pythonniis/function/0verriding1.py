class person:
    def f1(self):
      print("class person")
class student(person):
    def f2(self):
      print("class student")
class engeneering(student):
    def f3(self):
      print("class engeneering")
obj=engeneering()
obj.f1()
obj.f2()
obj.f3()

