from string import Template

class MyTemplate(Template):
	delimiter="#"

def Main():
	cart = []
	cart.append(dict(item="coke",price=8,qty=2))
	cart.append(dict(item="cake",price=12,qty=1))
	cart.append(dict(item="fish",price=32,qty=4))

	t=MyTemplate("#qty * #item = #price")
	total=0
	print "cart: "
	for data in cart:
		print t.substitute(data)
		total+=data["price"]
	print "Total "+ str(total)
if __name__=="__main__":
	Main()

