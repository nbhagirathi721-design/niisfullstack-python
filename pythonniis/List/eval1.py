'''
l=[]
print("enter a list")
l=eval(input())

l=[]
print("enter how many data store in  list")
s=int(input())
for i in range(0,s,1):
	print("enter eliment",i+1)
	l.append(int(input()))
print(l)
'''
l=[0,0,0,0,0]
for i in range(0,len(l),1):
	print("enter eliment",i+1)
	l=int(input())
print(l)
