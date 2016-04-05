#import os
#def find(name,path):
#	for root,dirs,files in os.walk(path):
#		if name in files:
#			print os.path.join(root,name),

#find("find.py","/home")'''

import os
for file in os.listdir("/home/ravi/proj"):
	l=0
	if file.endswith(".py"):
		for line in open(file):
			if '\n'!=line:
				if '#'not in line:
					l+=1
		print(file),"\t", l
