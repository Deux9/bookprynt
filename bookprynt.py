output = ""
input = int(raw_input("How many pages do you want to print?\n"))
if input % 2 == 0:
	for i in range (0, input/2):
		output = output + "%s,%s," % (str(i+1),str(input-i))
	output = output[0:len(output)-1]
	print output
else:
	print "Invalid input. Try an even number"
