import random
import sys

CHOIX=["Pierre", "Feuille", "Ciseau"]
BATTRE={"Pierre": "Feuille", "Feuille": "Ciseau", "Ciseau": "Pierre"}

def normaliser_entre(user_input):
  if not user_input:
    return None
  s=user_input.strip().lower()
  if s in ("q", "quit", "exit"):
    return "QUIT"
  if s.startswith("p"):
    return "Pierre"
  if s.startswith("f"):
    return "Feuille"
  if s.startswith("c"):
    return "Ciseau"
  return None

def partie(nb_partie, adapt_prob=0.75):
  point_user=0
  point_ordinateur=0
  user_counts={c: 1 for c in CHOIX}

  for _ in range(nb_partie):
    weights=[user_counts[c] for c in CHOIX]
    prediction=random.choices(CHOIX, weights=weights, k=1)[0]

    if random.random() < adapt_prob:
      ordinateur=BATTRE[prediction]
    else:
      ordinateur=random.choice(CHOIX)

    user_raw=input("Saisir un choix (Pierre/Feuille/Ciseau) ou 'q' pour quitter : ")
    user=normaliser_entre(user_raw)
    if user=="QUIT":
      print("Abandon du jeu.")
      break
    if user not in CHOIX:
      print("Entrée non reconnue, ce tour est annulé.")
      continue

    user_counts[user]+=1

    print(f"Vous: {user}  |  Ordinateur: {ordinateur}")

    if user == ordinateur:
      print("Il y a une égalité")
    elif (user == "Pierre" and ordinateur == "Feuille") or \
       (user == "Feuille" and ordinateur == "Ciseau") or \
       (user == "Ciseau" and ordinateur == "Pierre"):
      print("L'ordinateur gagne la manche")
      point_ordinateur+=1
    else:
      print("L'utilisateur gagne la manche")
      point_user+=1

  return point_user, point_ordinateur

if __name__ == "__main__":
  point_user, point_ordinateur = partie(5)
  print("Point de l'utilisateur :", point_user)
  print("Point de l'ordinateur :", point_ordinateur)
