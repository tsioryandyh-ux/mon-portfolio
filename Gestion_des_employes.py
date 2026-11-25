class Employe:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print("Nom :", self.nom)
        print("Age :", self.age)


class Developpeur(Employe):
    def __init__(self, nom, age, langage):
        super().__init__(nom, age)
        self.langage = langage

    def se_presenter(self):
        super().se_presenter()
        print("Langage prefere :", self.langage)


developpeur1 = Developpeur("Soa", 25, "Python")

developpeur1.se_presenter