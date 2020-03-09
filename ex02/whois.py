import sys
	

def hellow(data):
	if len(sys.argv[1:]) != 1:
		print("ERROR Invalid numbers of arguments")
		return
	if data.isnumeric() == 0:
		print("ERROR Wrong argument")
	i = int(data)
	if i % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")
	return
hellow(sys.argv[1])
