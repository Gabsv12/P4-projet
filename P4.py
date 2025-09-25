# Jeu puissance 4 

# on creer la grille de 6 ranges et 7 colonnes

tableau = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

# afficher la grille 

def afficher_grille():
    for ligne in tableau:
        ligne_affichee = ""
        for x in ligne:
            if x == 0:
                ligne_affichee += ". "
            else:
                ligne_affichee += str(x) + " "
        print(ligne_affichee.strip())
    print("-" * 29)

afficher_grille()

# jouer 1 = jeton 1 et joueur 2 = jeton 2 

def changer_joueur():
    global joueur_courant
    if joueur_courant == 1:
        joueur_courant = 2
    else:
        joueur_courant = 1

# demander au joueur 1 de choisir la case de la premiere range puis de meme au joueur 2 etc...

# si un des joeur rempli les regles pour gagner (4 jetons alignes horizontalement, verticalement ou den diagonale) il est declare gagnant

input("Appuyez sur Entrée pour fermer...")