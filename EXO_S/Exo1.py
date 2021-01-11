import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '')))

import Discriminant

class Data:
	def __init__(self, n, Lalist):
		self.n = n
		self.Lalist = Lalist

def convertir_entier():
	#b = []
	B = []
	filename = input("Entre le nom du fichier a lire: ") 
	inputFile = open(filename, "r")
	for line in inputFile:
		b = []
		line =  line.replace("\n","")
		line = line.replace("\r", "")
		try :
			lines = line.split(",")
			#print(lines)
			for ac in lines:
				b.append(int(ac))
			#print(b)
			B.append(b)
		except:
			print("probleme")
			exit(0)
	return B
           




print(sys.argv)

if len(sys.argv) == 1:
	"""
	filename = input("Entre le nom du fichier a lire: ") 
	inputFile = open(filename, "r")
	for line in inputFile:
		line =  line.replace("\n","")
		line = line.replace("\r", "")
		#print(line)
		ab = line.split(",")"""	
	Hb  = convertir_entier()
	#print(Hb)
	for hb in Hb:
		Discriminant.Discro(hb)

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






























