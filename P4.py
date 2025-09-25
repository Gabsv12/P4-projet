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


# jouer 1 = jeton 1 et joueur 2 = jeton 2 

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

# demander au joueur 1 de choisir la case de la premiere range puis de meme au joueur 2 etc...

print("Coucou l'ami, joue au Puissance 4 !")

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
