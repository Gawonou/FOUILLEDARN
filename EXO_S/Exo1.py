import sys
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', '')))

import Discriminant
import sys
import os

class Data:
	def __init__(self, n, Lalist):
		self.n = n
		self.Lalist = Lalist

def convertir_entier():
	#b = []
	B = []
	if len(sys.argv) == 1:
		filename = input("Entre le nom du fichier a lire: ")
		inputFile = open(filename, "r")
	elif len(sys.argv) == 2 or len(sys.argv) == 3:
		filename  = sys.argv[1]
		inputFile = open(filename, "r")
	
	
	i = 1
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
			#Show result in txt file
			
			i = i+1

		except:
			print("probleme a la ligne", i, line)
			exit(0)
	return B



def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1            

def OuTextFile(Reco):
	Reco = []
	monFile = open(r"C:\Users\Edem\Desktop\Output.txt", "w")
	monFile.write(listToString(Reco))
	monFile.close()







print(sys.argv)
"""
if len(sys.argv) == 1:

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
	
    if len(sys.argv) == 2:
    	Discriminant.Discro(hb)
    elif len(sys.argv) == 3:
         OuTextFile(Discriminant.Discro(hb))
         
	
"""
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
"""





























