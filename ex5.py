import itertools
it1=iter([1,2,4])
it2=iter([3,5,6])
i=itertools.chain(it1,it2)
print i
