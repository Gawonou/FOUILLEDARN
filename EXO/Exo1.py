import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '')))

import Discriminant

class Data:
	def __init__(self, n, Lalist):
		self.n = n
		self.Lalist = Lalist

def convertir_entier(A):
        b = []
	B = []
        try :
            lin = A.split(",")
        expect
	for ac in A:
		B.append(int(ac))
		#print(len(B))
	return B
           




print(sys.argv)

if len(sys.argv) == 1:

	filename = input("Entre le nom du fichier a lire: ") 
	inputFile = open(filename, "r")
	for line in inputFile:
		line =  line.replace("\n","")
		line = line.replace("\r", "")
		#print(line)
		ab = line.split(",")	
		Hb  = convertir_entier(ab)
		Discriminant.Discro(Hb)

elif len(sys.argv) == 2:
	filename  = sys.argv[1]
	inputFile = open(filename, "r")
	for line in inputFile:
		line =  line.replace("\n","")
		line = line.replace("\r", "")
		a = line.split(",")
		#print(a[0])	
		H  = convertir_entier(a)
		Discriminant.Discro(H)

else:
	print("Tu dois donner le nom de fichier en argument")






























