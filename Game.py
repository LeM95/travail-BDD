"""
# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
#    ]
# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur
# Process

    Lancer le jeu
        Fonction choix equipe
            Boucle de 3 pour trois personage  
                affichée la liste des personnage disponible
                ajoutée les personnage dans une autre liste et enlever de l'autre liste 

        Monstre aleatoire 
            recuperer la liste des monstre avec leur donnée et choisir au hasard

        Attaquer(victime,attaquant)
            soustrere le point de vie celon l'ATK
            return PV_victime 
        
        Combat equipe vs monstre  
            While True:
                for joeur dans equipe 
                    crée une liste des joueur avec encore des pv 

                for joeur dans equipe_vivante   
                    attaquer( monstre par joeur) 
                    verifier si le monstre est mort 
                        monstre aleatoire 
                        vague +=1
                        return combat equipe monstre

                choix aleatoir de joeur 
                attaquer(joeur par monstre)
                if joeur mort 
                    return combat  
                    if liste vide 
                        monstre gagne
                        break 



#    Afficher les scores
#        Recuperer scores base
#            ouvrir base
#            acceder a collection score
#            find
#            convertir curseur en list
#        filtrer les 3 meilleurs
#             trie le tableau sur element.waves
#             prendre 3 derniers elements
#                    array[-3:-1]
#        Affiche les score
#    Quitter
#       sys.exit()
"""