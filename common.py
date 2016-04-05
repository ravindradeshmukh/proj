from sys import argv
script=argv[0]
fn=argv
lines=""
def readfile(fn):
	for f in fn:
		for line in open(f):
			yield line

def grep(pattern,lines):
	return(line for line in lines if pattern in line)

def printlines(lines):
	for line in lines:
		print line,

def main(pattern, fn):
	lines=readfile(fn)
	lines=grep(pattern,lines)
	printlines(lines)

main('v',fn)
