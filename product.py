def product(a,b):
	i=1
	x=a
	while i<b:
		a=a+x
		i+=1
	return a

a=product(10,20)
print "10*20=",a 
