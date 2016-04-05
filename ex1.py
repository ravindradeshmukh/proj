#class yrange:
#	def __init__(self,n):
#		self.i=n-1
#		self.n=0
#	def __iter__(self):
#		return self
#	def next(self):
#		if self.i>=self.n:
#			i=self.i
#			self.i-=1
#			return i
#		else:
#			raise StopIteration()

#a=yrange(10)
#j=0
#while(j<10):
#	i=a.next()
#	print i
#	j+=1

def yrange(n):
	i=0
	while i<n:
		yield i
		i+=1

n=10
y=yrange(n)
print y
i=0
while i<n:
	print y.next()
	i+=1


