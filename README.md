# Pierre-Feuille-Ciseau avec IA adaptative

Ce projet est un petit jeu **Pierre-Feuille-Ciseau** en Python où l'ordinateur n'est pas totalement aléatoire : il **tente de s'adapter à vos choix** pour augmenter ses chances de gagner.

Le jeu se joue directement dans le terminal et vous pouvez arrêter la partie à tout moment.

---

## Fonctionnalités

* Interface en ligne de commande simple.
* IA adaptative :

  * Elle analyse vos choix précédents.
  * Elle tente de **prévoir votre prochain coup** et joue pour le battre.
* Possibilité de quitter à tout moment en tapant `q`, `quit` ou `exit`.
* Gestion des entrées invalides.
* Score affiché à la fin de la partie.

---

## Comment jouer

1. Lancez le jeu :

```bash
python3 pierre_feuille_ciseau.py
```

2. Choisissez votre coup à chaque tour :

   * `Pierre` ou `p`
   * `Feuille` ou `f`
   * `Ciseau` ou `c`

3. Le jeu vous indiquera le résultat de chaque manche et mettra à jour le score.

4. Pour quitter le jeu avant la fin, tapez `q`.

---

## Logique du code

### 1. Normalisation des entrées

La fonction `normaliser_entre(user_input)` permet de convertir vos saisies en un format standard (`Pierre`, `Feuille`, `Ciseau`) et gère également la sortie du jeu.

### 2. IA adaptative

* L’ordinateur garde une trace des choix de l’utilisateur.
* Il **pèse ses prédictions** en fonction de vos coups précédents.
* Avec une probabilité (par défaut 0.75), il choisira le coup qui **battrait votre prédiction**.
* Sinon, il joue aléatoirement pour ne pas être trop prévisible.

### 3. Déroulement de la partie

* Le jeu se déroule sur un nombre défini de manches (par défaut 5).
* Les scores sont comptabilisés à chaque tour.
* Résultat final affiché à la fin.

---

## Exemple d'utilisation

```
Saisir un choix (Pierre/Feuille/Ciseau) ou 'q' pour quitter : p
Vous: Pierre  |  Ordinateur: Feuille
L'ordinateur gagne la manche

Saisir un choix (Pierre/Feuille/Ciseau) ou 'q' pour quitter : f
Vous: Feuille  |  Ordinateur: Ciseau
L'ordinateur gagne la manche
...
Point de l'utilisateur : 2
Point de l'ordinateur : 3
```

---

## Personnalisation

Vous pouvez modifier :

* Le **nombre de manches** en changeant l’argument `partie(nb_partie=5)`.
* La **probabilité d’adaptation de l’IA** avec l’argument `adapt_prob` (valeur entre 0 et 1).

```python
# Exemple : partie de 10 manches avec IA moins prévisible
point_user, point_ordinateur = partie(10, adapt_prob=0.5)
```

---

## Licence

Projet libre pour usage personnel et éducatif.
