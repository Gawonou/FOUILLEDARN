import sys

class Data:
	def __init__(self, n, Lalist):
		self.n = n
		self.Lalist = Lalist



print(sys.argv)

if len(sys.argv) == 1:

	filename = input("Entre le nom du fichier a lire: ") 
	inputFile = open(filename, "r")
	for line in inputFile:
		line =  line.replace("\n","")
		line = line.replace("\r", "")
		print(line)

elif len(sys.argv) == 2:
	filename  = sys.argv[1]
	inputFile = open(filename, "r")
	for line in inputFile:
		line =  line.replace("\n","")
		line = line.replace("\r", "")
		print(line)
else:
	print("Tu dois donner le nom de fichier en argument")