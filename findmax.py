def max(a,b,c):
	if(a>b==a>c):
		return a
	elif(b>a==b>c):
		return b
	else:
		return c


a=input("first number")
b=input("second number")
c=input("third number")

m=max(a,b,c)
print(m,"is the largest")
