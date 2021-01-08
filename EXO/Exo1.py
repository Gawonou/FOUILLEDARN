import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '')))

iImport Discriminant

class Data:
	def __init__(self, n, Lalist):
		self.n = n
		self.Lalist = Lalist

def convertir_entier(A):
	B = []
	for a in A:
		B.append(int(a))

	return B




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
		a = line.split(",")
		#print(a[0])
		
		H  = convertir_entier(a)
		DiscriminantV2.DiscroV(H)

else:
	print("Tu dois donner le nom de fichier en argument")






























