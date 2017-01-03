#Python 3.5
import sys

try:
	inFile = open(sys.argv[1],'r')
except:
	print ("usage: regression.py [input file]")
	print ("       each line of [input file] should contain 2 space-separated ints")
	exit()

myData = []
for line in inFile:
	a,b = line.split()
	myData.append([a,b])

'''
for pair in myData:
	print(pair[0],pair[1])
'''