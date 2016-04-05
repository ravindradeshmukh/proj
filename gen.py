"""def foo():
	print 'begin'
	for i in range(3):
		print 'before yield',i
		yield i
		print 'after yield',i
	print'end'

f=foo()
f.next()
f.next()
f.next()"""

def integers():
	i=1
	while True:
		yield i
		i+=1

def squares():
	for i in integers():
		yield i*i

def take(n,seq):
	seq=iter(seq)
	result=[]
	try:
		for i in range(n):
			result.append(seq.next())
	except StopIteration:
		pass
	return result

print take(5,squares())
