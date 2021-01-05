# project python


1. Excercice

~~~
Ce exercice va evoluter avec le temps
~~~


Ecris un programme qui lit des entiers (normalement 3 ou 6  nombres par lignes) dans une fichier et fait la résolution d'équation du second dégré. Dans cette résolution, il faut considerer les trois cas posibles.  c'est à dire déterminant inferieur à 0, égal à 0 ou supérieur à 0. Dans le cas ou le déterminant est inferieur à 0 on affichie 'NaN'. 

Au début, le programme demande le nom du fichier dans lequel les valeurs sont si n est pas donné en argument.

Exemple du contenu fichier
```
10, 5, 1
-4, 1, 3
20, 10, 5, 3, 4,8
3, 5,7, 8
```
Contrainte à gerer 

*  Si une ligne contient un separateur autre que ',' Le programme affiche <Erreur dans le fichier et la ligne X> if est le nombre de la ligne et le  programme s'arrete.
*  Si une ligne contient le nombre des entiers  autre que 3 ou 6, le calcul n'est pas pour cette ligne.
* Si le nombre des entiers est egal 6 on fait le calcul pour les 3 premiers avant de faire le calcul des 3 derniers
*  Si tout est correct, le programme affiche:
```
	 x1=val, x2=val (x1 doit etre plus petit que x2 si determinant est superieur à 0)
	 x=val (si déterminant est = 0)
	 NaN (si  determinant est inferieur à 0)
```


Exemple d'affiche
```
 x1=val, x2=val 
 x=val
 NaN
 x1=val, x2=val
 x1=val, x2=val 
 x=val
 NaN 
 x1=val, x2=val 
 x=val
 NaN
 NaN
 x1=val, x2=val 
 x=val
 NaN
 x=val
 NaN
```

Ou 
```
Erreur dans le fichier et la ligne 6.
```