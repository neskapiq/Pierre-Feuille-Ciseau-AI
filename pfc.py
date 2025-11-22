import random
import sys

choix=["Pierre","Feuille","Ciseau"]

def partie(nb_partie):
  point_user=0
  point_ordinateur=0
  for i in range(nb_partie):
    ordinateur=random.choice(choix)
    user=input("Saisir un choix :")
    if nb_partie==0:
      sys.exit()
    elif user=="Pierre" and ordinateur=="Feuille":
      print("L'ordinateur gagne la partie")
      nb_partie=nb_partie-1
      point_ordinateur=point_ordinateur+1
    elif user=="Feuille" and ordinateur=="Pierre":
      print("L'utilisateur a gagné la partie")
      nb_partie=nb_partie-1
      point_user=point_user+1
    elif user=="Ciseau" and ordinateur=="Pierre":
      print("L'ordinateur gagne la partie")
      nb_partie=nb_partie-1
      point_ordinateur=point_ordinateur+1
    elif user=="Pierre" and ordinateur=="Ciseau":
      print("L'utilisateur gagne la partie")
      nb_partie=nb_partie-1
      point_user=point_user+1
    elif user=="Ciseau" and ordinateur=="Feuille":
      print("L'utilisateur gagne la partie")
      nb_partie=nb_partie-1
      point_user=point_user+1
    elif user=="Feuille" and ordinateur=="Ciseau":
      print("L'ordinateur gagne la partie")
      nb_partie=nb_partie-1
      point_ordinateur=point_ordinateur+1
    elif user==ordinateur:
      print("Il y a une égalité")
      nb_partie=nb_partie-1
  return point_user, point_ordinateur
  
point_user, point_ordinateur=partie(5)
print("Point de l'utilisateur :",point_user)
print("Point de l'ordinateur :",point_ordinateur)
