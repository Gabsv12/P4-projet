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

joueur_courant = 1

# afficher la grille 

def afficher_grille():
    for ligne in tableau:
        for x in ligne:
            if x == 0:
                print(".", end=" ")
            else:
                print(x, end=" ")
        print()  
    print("-" * 29)


# jouer 1 = jeton 1 et joueur 2 = jeton 2 

def changer_joueur():
    global joueur_courant
    joueur_courant = 3 - joueur_courant 

def jouer_colonne(col):
    i = len(tableau) - 1 
    while i >= 0:
        if tableau[i][col] == 0:
            tableau[i][col] = joueur_courant
            return True
        i -= 1
    return False

# Vérifier si vainqueur
def est_gagnant(joueur):

    lignes = len(tableau)
    colonnes = len(tableau[0])

    # Horizontal
    for i in range(lignes):
        for j in range(colonnes - 3):
            if (tableau[i][j] == joueur and
                tableau[i][j+1] == joueur and
                tableau[i][j+2] == joueur and
                tableau[i][j+3] == joueur):
                return True

    # Vertical
    for j in range(colonnes):
        for i in range(lignes - 3):
            if (tableau[i][j] == joueur and
                tableau[i+1][j] == joueur and
                tableau[i+2][j] == joueur and
                tableau[i+3][j] == joueur):
                return True

    # Diagonale
    for i in range(lignes - 3):
        for j in range(colonnes - 3):
            if (tableau[i][j] == joueur and 
                tableau[i+1][j+1] == joueur and
                tableau[i+2][j+2] == joueur and
                tableau[i+3][j+3] == joueur):
                return True

    # Diagonale 
    for i in range(3, lignes):
        for j in range(colonnes - 3):
            if (tableau[i][j] == joueur and
                tableau[i-1][j+1] == joueur and
                tableau[i-2][j+2] == joueur and
                tableau[i-3][j+3] == joueur):
                return True

    return False

# Sortie principale

# demander au joueur 1 de choisir la case de la premiere range puis de meme au joueur 2 etc...

print("Coucou l'ami, joue au Puissance 4 !")

while True:
    try:
        choix = int(input(f"Joueur {joueur_courant}, quelle colonne choisis-tu ? (0-6) : "))
    except ValueError:
        print("Uniquement un chiffre !")
        continue

    if choix < 0 or choix > 6:
        print("Colonne incorrecte, rappel entre 0-6 !")
        continue

    if not jouer_colonne(choix):
        print("Ah déjà pris :( , choisis-en une autre !")
        continue

    afficher_grille()

# si un des joeur rempli les regles pour gagner (4 jetons alignes horizontalement, verticalement ou den diagonale) il est declare gagnant

    if est_gagnant(joueur_courant):
        print(f"Bravo ! Joueur {joueur_courant} a gagné ! ")
        break

    changer_joueur()

input("Appuie sur Entrée pour quitter...")