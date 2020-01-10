#python 3.7.1
#Devine le chiffre Version 2
from random import randint
print("----------------------------------------------\n")
print("               Devine un chiffre.               ")
print("                  3 niveaux                     ")
print("                codeby åurejien               \n")
print("----------------------------------------------\n")
print()
name = input("Ton nom?. . \n→ ")
name = name.title()
print()
print("choisis ton niveau:")
level = int(input("{1} Facile\n{2} Difficile \n{3} Extreme \n→ "))
print()
if level == 1:
  print("Niveau Facile, \nDevine un chiffre entre 1 et 100 \nen seulement 6 essais")
  x = 6
  a = randint(1, 100)
elif level == 2:
  print("Niveau Difficile, \nDevine un chiffre entre 1 et 200 \nen seulement 10 essais")
  x = 10
  a = randint(1, 200)
elif level == 3:
  print("Niveau Hard, \nDevine un chiffre entre 1 et 1000 \nen seulement 10 essais")
  x = 10
  a = randint(1, 1000)
print()
print("{600} Ouvrir le menu")
print()
print("Nombre d'essais")
while x != 0:
  try:
    if x == 1:
      print()
      print("dernier essai")
    else:
      print()
      print(x, "essais")
    n = int(input("Devine?  → "))
    x += -1
    if n == a:
      print("Tu as trouve...")
      print("Bien joue", name)
      print("----------------------------------------------\n")
      print(name, "veux tu rejouer? ")
      restart = int(input("{1} oui\n{0} non\n→ "))
      print()
      if restart == 1:
        print(name, "Bonne partie")
        print()
        print("{600} Pour ouvrir le menu")
        print()
        print("----------------------------------------------\n")
      else:
        print("----------------------------------------------\n")
        print("A bientot", name)
        print("----------------------------------------------\n")
        break
    elif n == 600:
      print()
      print("----------------------------------------------\n")
      menu = int(input("{601} Changer la difficulté\n{602} Quitter le jeu\n{603} Gagner des essais\n{604} Changer de nom\n→ "))
      print()
      if menu == 601:
        print(name, "choisis ton niveau:")
        level = int(input("{1} Facile\n{2} Difficile \n{3} Extreme \n→ "))
        print()
        if level == 1:
          print(
              "Niveau Facile, \nDevine un chiffre entre 1 et 100 \nen seulement 6 essais")
          x = 6
          a = randint(1, 100)
        elif level == 2:
          print(
              "Niveau Difficile, \nDevine un chiffre entre 1 et 200 \nen seulement 10 essais")
          x = 10
          a = randint(1, 200)
        elif level == 3:
          print(
              "Niveau Hard, \nDevine un chiffre entre 1 et 1000 \nen seulement 10 essais")
          x = 10
          a = randint(1, 1000)
      elif menu == 603:
          print()
          print("----------------------------------------------\n")
          print("Mini jeu.")
          print("Remporte la partie avec le plus haut chiffre contre l'ordinateur\net gagne 5 essais en plus\n")
          nun = int(input("{1} lancer?\n→ "))
          miniH = randint(1, 20)
          miniO = randint(1, 20)
          print("Votre tirage", miniH, "- l'ordinateur", miniO)
          if miniH >= miniO:
            x += 6
            print(name, "tu as gagnés")
            print("Tu remportes 5 essais")
            print("----------------------------------------------\n")
            nun = int(input("{0} quitter\n→ "))
            print("----------------------------------------------\n")
            print()
          else:
            x += 1
            print(name, "tu as perdu")
            print("Tu ne remportes pas d'essai supplémentaire")
            print("----------------------------------------------\n")
            nun = int(input("{0} quitter\n→ "))
            print("----------------------------------------------\n")
            print()
      elif menu == 604:
        x += 1
        print(name,"tu veux changer de nom?")
        name=input("Entre ton nouveau nom:\n→")
        name = name.title()
        print()
        print("Voila",name,"tu as un nouveau nom.")
      else:
        print("----------------------------------------------\n")
        print("Tu as décidé de quitter la partie")
        print("A bientot", name)
        print()
        print("----------------------------------------------\n")
        break
    elif n < 1 or n > 1000:
      print("Choisis un chiffre entre 1 et 500 seulement")
      x += 1
    elif x == 0:
      print("Tu as perdu")
      print("Le numero etait")
      print(a)
      print("----------------------------------------------\n")
      print(name, "veux tu rejouer? ")
      restart = int(input("{1} oui\n{0} non\n→ "))
      print()
      if restart == 1:
        print(name, "Bonne partie")
        print()
        print("{600} Pour ouvrir le menu")
        print()
        print("----------------------------------------------\n")
      else:
        print("----------------------------------------------\n")
        print("A bientot",name)
        print("----------------------------------------------\n")
        break
    elif n < a:
      print("Plus grand")
    elif n > a:
      print("Plus petit")
  except ValueError:
    print("Erreur d'entrée des données")
    continue
