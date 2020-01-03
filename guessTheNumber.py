#python 3.7.1

x=6
from random import randint
a=randint(1,100)
print("----------------------------------------------\n")
print("        Guess a number between 1 et 100         ")
print("             You only have 6 try               ")
print("               codeby åurejien              \n ")
print("----------------------------------------------\n")
print("Your try")
while x!=0:
  try:
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
   n=int(input("Guess?  → "))
   x+=-1
   if n==a:   
     print("You won...")
     print("Well play")
     print("----------------------------------------------\n")
     print("Do you want to restart? ")
     restart=int(input("{1} yes\n{0} no\n→ "))
     if restart==1:
        x=6
        a=randint(1,100)
        print("----------------------------------------------\n")
     else:
        print("----------------------------------------------\n")
        print("Goodbye.")
        print("----------------------------------------------\n")
        break
   elif n<1 or n>100:
     print("Only a number between 1 & 100")
     x+=1
   elif x==0:
     print("□□□□□□")
     print("You lost")
     print("The number was")
     print(a)
     print("----------------------------------------------\n")
     print("Do you want to restart? ")
     restart=int(input("{1} yes\n{0} no\n→ "))
     if restart==1:
        x=6
        a=randint(1,100)
        print("----------------------------------------------\n")
     else:
        print("----------------------------------------------\n")
        print("Goodbye.")
        print("----------------------------------------------\n")
        break
   elif n<a:
     print("Higher")
   elif n>a:
     print("Lower")
  except ValueError:
    print("Value Error")
    continue  
     
     
     
     
     
     
     
