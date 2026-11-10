class Voiture:
    # Constructeur et attributs
    def __init__(self, marque, couleur, vitesse):
        self.marque = marque
        self.couleur = couleur
        self.vitesse = vitesse

    # Méthodes (comportements)
    def demarrer(self):
        print("La voiture démarre.")

    def accelerer(self):
        self.vitesse += 10
        print("La vitesse est de", self.vitesse, "km/h")

    def freiner(self):
        self.vitesse = 0
        print("La voiture est arrêtée.")


# création des objets
voiture1 = Voiture("Toyota" , "Rouge" , 0)
voiture2 = Voiture("Bmw", "Noire", 0)

#Teste du fonctionnement
print("voiture1 :", voiture1.marque, voiture1.couleur)
voiture1.demarrer()
voiture1.accelerer()
voiture1.freiner()

print ("voiture2 :", voiture2.marque, voiture2.couleur)
voiture2.demarrer()
voiture2.accelerer()