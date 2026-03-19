'''
l=[5,8,6,3,8,7,7,12]
l1=[]
for i in l:
	if i not in l:
		l1.append(i)
print(l1)

l=[5,8,6,3,8,7,7,12]
l1=[i for i in l]
print(l1)

l=[5,8,6,3,8,7,7,12]
l1=[i+3 for i in l]
print(l1)
'''
l=[5,8,6,3,8,7,7,12]
l=[i+3 for i in l if i%2==0]
print(l)
