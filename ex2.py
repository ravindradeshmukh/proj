from sys import argv
script=argv[0]
"""f1=argv[1]
f2=argv[2]"""
filename=argv
def cat(fn):
	for f in fn:
		for line in open(f):
			print line,
		print'\n\n'
#filename=(f1,f2)
cat(filename)
