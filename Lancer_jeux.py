class Jeux: 
    def __init__(self):
        self.equipe = []
        self.monstre = None
        self.vague = 0
        pass


    def choix_equipe(self,Liste_roles):
        """
        Fonction choix equipe  
                Boucle de 3 pour trois personage  
                    affichée la liste des personnage disponible
                    ajoutée les personnage dans une autre liste et enlever de l'autre liste

        """
        for personnage in range(3):
            print(f" Choix du personnage {personnage + 1}/3 ")
        
        for index, perso in enumerate(Liste_roles):
            print(f"{index }. {perso['name']} | ATK {perso['attack']} | DEF {perso['defense']} | PV {perso['hp']}")
        choix = int(input("Choisis un numéro : "))
        self.equipe.append(Liste_roles[choix])
        Liste_roles.pop(choix)


    def monstre_aleatoire(self):
        pass

    def attaquer_joeur(self):
        pass 
    def combat(self):
        pass