'''
s="welcome"
l=[]
for i in s:
	if i in"aeiou":
		l.append(i)
print(l)
'''
s="welcome"
l=[i for i in s if i in"aeiou"]
print(l)
