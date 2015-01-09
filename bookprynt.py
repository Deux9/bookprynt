#!/usr/bin/env python

output = ""
inputcount = int(raw_input("How many pages is your document?\n"))
first = int(raw_input("Which page do you want printed first?\n"))
count = inputcount - (first - 1)
if count % 2 == 0:
	for i in range (0, count/2):
		output = output + "%s,%s," % (str(i+first),str(count+first-(i+1)))
	output = output[0:len(output)-1]
	print output
else:
	print "Invalid count. Read the manual"
