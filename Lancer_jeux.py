import random


class Jeux: 
    def __init__(self,liste_monstres,liste_roles):
        self.equipe = []
        self.monstre = None
        self.vague = 0
        self.liste_monstres = liste_monstres
        self.liste_roles = liste_roles



    def choix_equipe(self):
        for personnage in range(3):
            print(f" Choix du personnage {personnage + 1}/3 ")
            for index, perso in enumerate(self.liste_roles):
                print(f"{index }. {perso['name']} | ATK {perso['attack']} | DEF {perso['defense']} | PV {perso['hp']}")
            choix = int(input("Choisis un numéro : "))
            self.equipe.append(self.liste_roles[choix])
            self.liste_roles.pop(choix)


    def monstre_aleatoire(self):
        self.monstre = random.choice(self.liste_monstres).copy()
        print(f"Vague {self.vague} : un {self.monstre['name']} apparaît !")

    def attaquer(self, victime, attaquant):
        victime["hp"] -= attaquant["attack"]
        print(f"{attaquant['name']} attaque {victime['name']} → PV restants : {victime['hp']}")
        return victime["hp"]
    
    def Equipe_vivante(self):
        list_equipe_vivante = []
        for joueur in self.equipe:
            if joueur["hp"] > 0:
                list_equipe_vivante.append(joueur)
        return list_equipe_vivante

    def combat(self):
        while True:
            if len(self.Equipe_vivante()) == 0:
                print(f"Le monstre gagne ! Vagues atteintes : {self.vague}")
                break

            for joueur in self.Equipe_vivante():
                pv_monstre = self.attaquer(self.monstre, joueur)
                if pv_monstre <= 0:
                    print(f"{self.monstre['name']} est vaincu !")
                    self.vague += 1
                    self.monstre_aleatoire()
                    return self.combat()

            joueur = random.choice(self.Equipe_vivante())
            pv_joueur = self.attaquer(joueur, self.monstre)
            if pv_joueur <= 0:
                print(f"{joueur['name']} est mort !")
    def lancer(self):
        self.choix_equipe()
        self.monstre_aleatoire()
        self.combat()