import random

accents = {
    'à': 'a', 'â': 'a', 'ä': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
    'î': 'i', 'ï': 'i', 'ô': 'o', 'ö': 'o', 'ù': 'u', 'û': 'u', 'ü': 'u',
    'ç': 'c',
}
def regles():
    print("les règles du jeu sont les suivantes :\n\n"
          "vous devez trouver le mot choisi aléatoirement dans le fichier lettre par lettre\n"
          "A chaque tour, vous pourrez choisir une lettre à essayer\n"
          "Si celle ci est dans le mot, en une ou plusieurs fois, l'affichage s'actualisera et un nouveau tour se lance\n"
          "Si celle ci n'est pas dans le mot, vous perdrez une vie\n"
          "Vous avez 6 vies\n"
          "Bonne chance \n\n" )

def charger_mots(fichier):
    with open(fichier, "r", encoding="utf-8") as fichier:
        mots = [retirer_accents(line.strip().lower()) for line in fichier]
    return mots
    
def retirer_accents(mots):
    return ''.join(accents.get(lettre, lettre) for lettre in mots)
    
def rejouer():
    choix = input("voulez vous rejouer ? (oui/non) \n")
    if choix ==  'oui' :
        pendu()
    else :
        print("\nau revoir !")

def pendu():
    regles()
    vies = 6
    bonnes_lettres = []
    mauvaises_lettres= []
    
    demande_fichier=input('Avez vous un fichier de mots avec lequel jouer ? (oui/non) \n')
    if demande_fichier == 'oui':
        fichier = input ("insérer le nom complet du fichier avec l'extension txt \n")
    else :
        fichier = 'mots_pendu.txt'
    mots = charger_mots(fichier)
    mot_choisi = random.choice(mots)
    
    while vies > 0:
        affichage = "".join([lettre if lettre in bonnes_lettres else "_" for lettre in mot_choisi])
        print(f"\nMot à deviner: {affichage}")
        print(f"vies restantes: {vies}")
        print(f"Lettres non présentes: {mauvaises_lettres} et lettres trouvées: {bonnes_lettres}")

        if affichage == mot_choisi:
            print("\nVictoire !\n")
            rejouer()
            break

        essai = input("Choix du joueur :  ")

        if len(essai) > 1:
            print("veuillez ne choisir qu'une seule lettre")
            continue

        if essai in mot_choisi :
            print("\nbonne pioche! \n")
            bonnes_lettres.append(essai)
        else :
            vies = vies - 1
            print("\nmauvaise pioche, vous perdez une vie! \n")
            mauvaises_lettres.append(essai)

    if vies == 0 :
        print(f"\nVous n'avez plus de vies restantes, c'est perdu \nLe bon mot était {mot_choisi}\n")
        rejouer()


pendu()
