def discriminant(a, b, c): 

  
    discriminant = (b**2) - (4*a*c) 
    if discriminant > 0: 
          
        print('Discriminant is', discriminant, 
                "which is Positive") 
                  
        print('Hence Two Solutions') 
          
    elif discriminant == 0: 
          
        print('Discriminant is', discriminant,  
                "which is Zero") 
                  
        print('Hence One Solution') 
          
    elif discriminant < 0: 
          
        print('Discriminant is', discriminant,  
                "which is Negative") 
                  
        print('Hence No Real Solutions')



def DiscroV(A):
	
    if len(A) == 3:
        x = A[0]
        y = A[1]
        z = A[2]
        discriminant(x, y, z)
        
    elif len(A) == 6:
        B = A[:len(A)//2]
        print(B)
        C = A[len(A)//2:]
        print(C)
        x = B[0]
        y = B[1]
        z = B[2]
        d1 = discriminant(x, y, z)
        a = C[0]
        b = C[1]
        c = C[2]
        d2 = discriminant(a, b, c)
        return d1
        return d2
        print ("Les deux discriminants sont: ", d1, " et ", d2)
    else:
        print("Erreur, Pas de calcul de discriminant")


KT = [1, 5, 4]
DiscroV(KT)
