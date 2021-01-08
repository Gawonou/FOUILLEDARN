import math  
  
  
# function for finding roots 
def equationroots( a, b, c):  
  
    # calculating discriminant using formula 
    dis = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis))  
      
    # checking condition for discriminant 
    if dis > 0:     
        print("x1 = ", (-b + sqrt_val)/(2 * a), ", x2 = ",(-b - sqrt_val)/(2 * a))  
          
    elif dis == 0:    
        print("x = ",-b / (2 * a))  
      
    # when discriminant is less than 0 
    else: 
        print("NaN")   
    


def Discro(A):
    if len(A) == 3:
        x = A[0]
        y = A[1]
        z = A[2]
        d = equationroots(x, y, z)
        return d
    elif len(A) == 6:
        B = A[:len(A)//2]
        print(B)
        x = B[0]
        y = B[1]
        z = B[2]
        d1 = equationroots(x, y, z)
        
        C = A[len(A)//2:]
        print(C)
        x = C[0]
        y = C[1]
        z = C[2]
        d2 = equationroots(x, y, z)
        
        return d1, d2
        
    else:
        print("Erreur, Pas de calcul de discriminant")


SK = [1, -5, 6, 1, 2, 1]
Discro(SK)










 
