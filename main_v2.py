from fonctions_v2 import *



while(True):
    afficherMainMenu()
    saisie=input('> ')
    if saisie=='q':
        break

    if saisie=='j':
        afficherSecMenu()
        while(True):
            afficherSecMenu()
            saisie=input('> ')
            if saisie=='q':
                break
            if saisie=='m':
                continue
            if saisie=='2':
                while(True):
                    saisie=input('Nom de votre Personnage ?\n> ')
                    validation=input('Votre nom: {}\nok (o/n) ?'.format(saisie))
                    if validation == 'n':
                        continue
                    elif validation == 'o':
                        if not joueurExiste(saisie):
                            enregisrerJoueur(saisie)
                            break
                        else:
                            print('Le joueur existe déjà\n')
                            continue
            
            if saisie == '1':
                '''
                - q: quitter
                - a: afficher liste des joueurs
                - Choisir un joueur parmi la liste de nom
                    > afficher liste nomJoueur
                    > Si joueur n'existe pas => 'joueur n'existe pas
                    > Sinon on récupère les données du joueur nom et point
                '''
                joueur=choixjoueur()

                motMystere=choixMot()
                print(motMystere)
                points=motATrouver(motMystere)
                majPointsJoueur(joueur['nom'],points)
                break