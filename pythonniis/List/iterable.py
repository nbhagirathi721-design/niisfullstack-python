l=[5,8,6,3,8,7,7,12]
i=0
while i<len(l):
	if l[i]%2!=0:#iff odd-remove
		l.remove(l[i])
	else:
		i+=1
print(l)
