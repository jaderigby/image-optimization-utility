def example():
	print "process working!"

def statusMessage():
	print
	print("Example usage: optim -o ~/Documents/serovital-hair/staticcontent/serovitalhair.com/images/ba/")
	print

def show(INPUT):
	if isinstance(INPUT, list):
		for item in INPUT:
			print item
