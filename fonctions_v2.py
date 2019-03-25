import json
from donnees import *
from random import randint

def afficherSecMenu():
        '''Affiche le menu principal'''
        print('============ Jeu du pendu ============\n')
        print("- 1: Choisir un perso")
        print("- 2: Créer un perso")
        print("- q: quitter")
        print("- m: afficher menu")
def afficherMainMenu():
    '''Affiche le menu de jeu'''
    print('============ Menu ============')
    print("- q: quitter\n- j: jouer")
    print('==============================')
def afficherMenuChoixJoueur(): 
    print('============ Choix du joueur ============')
    print("- q: quitter\n- a: afficher la liste des joueurs")
def choixMot():
    '''choisi au hasard un mot à deviner'''
    motMystere=liste_mots[randint(0, len(liste_mots) - 1)]
    return motMystere

def listeDonneesJoueurs():
    '''recupere la liste des joueurs {nom:*,points:*} et la place dans une variable
    type: liste
    '''
    with open('liste_joueur_v2.txt','r') as fichier:
        liste=json.load(fichier)
    return liste

def enregisrerJoueur(nomJoueur,points='0'):
    '''Permet d'enregistrer un joueur dans le fichier .txt'''
    
    nomJoueur=str(nomJoueur) # On caste la variable en string, au cas où
    liste_joueur=listeDonneesJoueurs() # On récupère la liste des joueurs grâce à la fonction précédente

    nouveauJoueur={'nom':nomJoueur,'points':points} # On configure le nouveau joueur au même format
    liste_joueur.append(nouveauJoueur) # On le rajoute à la fin de la liste
    with open('liste_joueur_v2.txt','w') as fichier: # On ouvre le fichier en écriture pour y écrire le nouveau joueur
        json.dump(liste_joueur,fichier)
    print('Joueur enregistré\n')

def joueurExiste(nomJoueur):
    '''
    Vérifie si le joueur existe, prend le nom du joueur en paramètre, retourne un booléen
    '''
    liste_joueur=listeDonneesJoueurs()
    nomJoueur_existe=False

    for elt in liste_joueur:
        if nomJoueur in elt.values():
            nomJoueur_existe=True
            break
    return nomJoueur_existe

def listeNomJoueur():
    '''retourne la liste des noms de joueur'''
    liste_joueurs=listeDonneesJoueurs()
    liste_noms_joueurs=[]
    for elt in liste_joueurs:
        for cle, valeur in elt.items():
            if cle == 'nom':
                liste_noms_joueurs.append(valeur)
    return(liste_noms_joueurs)

def infoJoueur(nomJoueur):
    ''' Retourne les données {nom,point} d'un joueur, dictionnaire
    \nPrend un nom de joueur en entrée'''
    liste_infos_joueurs=listeDonneesJoueurs()
    for elt in liste_infos_joueurs:
        for cle, valeur in elt.items():
            if valeur == nomJoueur:
                return elt

def choixjoueur():
    '''Permet de choisir un joueur parmis la liste des joueurs présent\nRetourne le nom et le nombre de point {}'''
    while(True):
        afficherMenuChoixJoueur()
        saisie=input('Choisissez un joueur\n> ')
        if not saisie:
            continue
        elif saisie=='q':
            break
        elif saisie =='a':
            afficherJoueurPoints()
            print("\n")
        elif  joueurExiste(saisie):
            joueur=infoJoueur(saisie)
            validation=input("\nVotre nom: {}\nVos points: {}\nok(o/n) ?"\
                .format(joueur['nom'],joueur['points']))
            if validation=='o':
                return joueur
            elif validation=='n':
                continue
        else:
            input("Ce joueur n'existe pas !\n")
            continue


def majPointsJoueur(nomJoueur,pointsGagne):
    '''
    Fonction qui met à jour le nombre de points d'un joueur.
    Prend en paramètres le nom du joueur et les points gagnés
    '''
    pointsGagne=int(pointsGagne)
    liste_infos_joueurs=listeDonneesJoueurs()
    for elt in liste_infos_joueurs:
        if elt['nom'] == nomJoueur:
            elt['points']=str(int(elt['points'])+pointsGagne)
    
    with open('liste_joueur_v2.txt','w') as fichier:
        json.dump(liste_infos_joueurs,fichier)

def motATrouver(mot):
    '''
    Prend un mot en paramètre\n
    Compare la saisie utilisateur avec le mot\n
    Retourne le nombre de points et un message
    '''
    j=0
    listeLettre=[]
    listeMystere=[]
    listeLettrerTestee=[]

    for elt in mot:
        listeLettre.append(elt)
        listeMystere.append('*')


    while (j<8):
        if listeMystere == listeLettre:
            print('\nVous avez trouvé !')
            break
        print('\nil vous reste {} coups\n'.format(8-j))
        for lettre in listeMystere:
            print(lettre,end=' ')
        saisie = input('\n> ')

        if len(saisie)>1:
            print('une seule lettre à la fois')
            continue

        elif not saisie:
            continue

        elif saisie in listeLettre:
            i=0
            while i<len(listeLettre):
                if saisie == listeLettre[i]:
                    listeMystere[i]=listeLettre[i]
                i+=1
            print('{}, fait parti du mot à trouver'.format(saisie))
            continue

        elif (not saisie  in listeLettre) and (saisie in listeLettrerTestee):
            print('lettre deja testee')
            continue
        
        elif (not saisie  in listeLettre) and (not saisie in listeLettrerTestee):
            listeLettrerTestee.append(saisie)
            print('raté !')
            j+=1

        for lettre in listeMystere:
            print(lettre,end=' ')

    if j==8 and listeMystere == listeLettre:
        print('Vous avez trouvé, mais vous ne gagnez pas de points...')
        return 0
    elif j<8:
        print('Vous gagnez {} points'.format(8-j))
        return 8-j
    else:
        print("perdu :(\nLe mot était "+mot)
        return 0

def afficherJoueurPoints():
    listeJoueurs=listeDonneesJoueurs()
    for elt in listeJoueurs:
        print("\t{} \t{} points".format(elt['nom'],elt['points']))

# Autres fonctions
def Break():
    saisie=input('break ?\n> ')
    if not saisie:
        quit()

