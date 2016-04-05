from sys import argv
script=argv[0]
"""f1=argv[1]
f2=argv[2]"""
filename=argv
def grep(fn):
	for f in fn:
		print f
		for line in open(f):
			if len(line)>40:
				print line,
		print'\n\n'
#filename=(f1,f2)
grep(filename)
