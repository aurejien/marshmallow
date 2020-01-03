#python 3.7.1

x=6
from random import randint
a=randint(1,100)
print("----------------------------------------------\n")
print("      Devine un chiffre entre 1 et 100       ")
print("         Tu as seulement 6 essais            ")
print("              codeby åurejien               \n ")
print("----------------------------------------------\n")
print("Nombre d'essais")
while x!=0:
   if x == 6:
     print("■■■■■■")
   elif x == 5:
     print("■■■■■□")
   elif x == 4:
     print("■■■■□□")
   elif x == 3:
     print("■■■□□□")
   elif x == 2:
     print("■■□□□□")
   elif x == 1:
     print("■□□□□□") 
   n=int(input("Devine?  → "))
   x+=-1
   if n==a:   
     print("Tu as trouve...")
     print("Bien joue")
     print("----------------------------------------------\n")
     print("Veux tu rejouer? ")
     restart=int(input("{1} oui\n{0} non\n→ "))
     if restart==1:
        x=6
        a=randint(1,100)
        print("----------------------------------------------\n")
     else:
        print("----------------------------------------------\n")
        print("A bientot")
        print("----------------------------------------------\n")
        break
   elif n<1 or n>100:
     print("Choisis un chiffre entre 1 et 100 seulement")
     x+=1
   elif x==0:
     print("□□□□□□")
     print("Tu as perdu")
     print("Le numero etait")
     print(a)
     print("----------------------------------------------\n")
     print("Veux tu rejouer? ")
     restart=int(input("{1} oui\n{0} non\n→ "))
     if restart==1:
        x=6
        a=randint(1,100)
        print("----------------------------------------------\n")
     else:
        print("----------------------------------------------\n")
        print("A bientot")
        print("----------------------------------------------\n")
        break
   elif n<a:
     print("Plus grand")
   elif n>a:
     print("Plus petit")
     
     
     
     
     
     
     
     
     
