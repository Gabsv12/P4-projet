# nom = input("Entre ton nom : ")
# print("Ton nom est :", nom)


# input("Appuie sur Entrée pour quitter...")

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

def afficher_grille():
    for ligne in tableau:
        for x in ligne:
            if x == 0:
                print(".", end=" ")
            else:
                print(x, end=" ")
        print()  
    print("-" * 29)

def changer_joueur():
    global joueur_courant
    if joueur_courant == 1:
        joueur_courant = 2
    else:
        joueur_courant = 1

def jouer_colonne(col):
    for i in range(len(tableau)-1, -1, -1):
        if tableau[i][col] == 0:
            tableau[i][col] = joueur_courant
            return True
    return False  


# Sortie principale

print("Coucou l'ami, joue au Puissance 4 !")
afficher_grille()

while True:
    try:
        choix = int(input(f"Joueur {joueur_courant}, quelle colonne choisis-tu ? (0-6) : "))
        if choix < 1 or choix > 7:
            print(" Colonne incorrect, rappel entre 0-6 !")
            continue

        if not jouer_colonne(choix):
            print(" Ah deja pris :( , choisis-en une autre !")
            continue

        afficher_grille()
        changer_joueur()

    except ValueError:
        print("Uniquement un chiffre !")