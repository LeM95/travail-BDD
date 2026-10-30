from pymongo import MongoClient
from Lancer_jeux import Jeux

client = MongoClient("mongodb://localhost:27017/")
db = client["Game"]

roles = list(db["roles"].find())
monstres = list(db["monstre"].find())


MENU = [
    "Lancer Jeu",
    "Afficher les scores",
    "Quitter",
]


def afficher_menu():
    for numero, texte in enumerate(MENU, start=1):
        print(f"{numero}. {texte}")


def erreur():
    print("Choix invalide, réessaie.")


def choix():
    while True:
        saisie = input("Ton choix : ")
        if saisie.isdigit() and 1 <= int(saisie) <= len(MENU):
            return int(saisie)
        else:
            erreur()


afficher_menu()
reponse = choix()
print(f"Tu as choisi : {MENU[reponse - 1]}")

jeu = Jeux(monstres, roles)   
jeu.lancer()                  