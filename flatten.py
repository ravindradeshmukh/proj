'''def flatten_list(a,result=None):
	if result is None:
		result=[]
	for x in a:
		if isinstance(x,list):
			flatten_list(x,result)
		else:
			result.append(x)
	return result

a=([[1,2,[3,4]],[5,6],7])
result=None
r=flatten_list(a,result)
print r'''

import collections

def flatten_dict(d, parent_key='', sep='.'):
	items = []
    	for k, v in d.items():
        	new_key = parent_key + sep + k if parent_key else k
        	if isinstance(v, collections.MutableMapping):
			items.extend(flatten_dict(v,new_key,sep=sep).items())
        	else:
            		items.append((new_key, v))
    	return dict(items)

d={'a':1,'b':{'x':2,'y':3},'c':4}
r=flatten_dict(d)
print r
