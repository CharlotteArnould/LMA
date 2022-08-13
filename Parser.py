from configparser import ConfigParser

class Publication:
    def __init__(self, FilePath):
        self.parse(FilePath)

    def parse(self, FilePath):

        ### Initialisation du Parser du fichier de description
        parser = ConfigParser()
        parser.read(FilePath)

        ### Récupération des données de la section "Animal"
        nom = parser["Animal"]["Nom"]
        type = parser["Animal"]["Type"]
        dateDeNaissance = parser["Animal"]["DateDeNaissance"]
        sexe = parser["Animal"]["Sexe"]
        numeroIdentification = parser["Animal"]["NumeroIdentification"]
        description = parser["Animal"]["Description"]
        taille = parser["Animal"]["Taille"]
        race = parser["Animal"]["Race"]
        race2 = parser["Animal"]["Race2"]
        self.animal = self.Animal(nom, type, dateDeNaissance, sexe, numeroIdentification, description, race, race2, taille)

        ### Récupération des données de la section "Entente"
        chat = parser["Entente"]["Chat"]
        chien = parser["Entente"]["Chien"]
        enfant = parser["Entente"]["Enfant"]
        self.entente = self.Entente(chat, chien, enfant)

        ### Récupération des données de la section "Veterinaire"
        identification = parser["Veterinaire"]["Identification"]
        vermifuge = parser["Veterinaire"]["Vermifuge"]
        deparasitage = parser["Veterinaire"]["Deparasitage"]
        sterilisation = parser["Veterinaire"]["Sterilisation"]
        self.veterinaire = self.Veterinaire(identification, vermifuge, deparasitage, sterilisation)

        ### Récupération des données de la section "FA"
        prenom = parser["FA"]["Prenom"]
        codePostal = parser["FA"]["CodePostal"]
        ville = parser["FA"]["Ville"]
        telephone = parser["FA"]["Telephone"]
        self.fa = self.FA(prenom, codePostal, ville, telephone)



    class Animal :
        def __init__(self, nom, type, dateDeNaissance, sexe, numeroIdentification, description, race, race2 = None, taille = None):
            self.nom = nom
            self.type = type
            self.dateDeNaissance = dateDeNaissance
            self.sexe = sexe
            self.numeroIdentification = numeroIdentification
            self.description = description
            self.race = race
            self.race2 = race2
            self.taille = taille

    class Entente :
        def __init__(self, chat, chien, enfant):
            self.chat = chat
            self.chien = chien
            self.enfant = enfant

    class Veterinaire :
        def __init__(self, identification, vermifuge, deparasitage, sterilisation):
            self.identification = identification
            self.vermifuge = vermifuge
            self.deparasitage = deparasitage
            self.sterilisation = sterilisation

    class FA :
        def __init__(self, prenom, codePostal, ville, telephone):
            self.Prenom = prenom
            self.codePostal = codePostal
            self.ville = ville
            self.telephone = telephone
            self.mail = "gestion.lamaisondesanimaux77@gmail.com"

test = False
if test :
    publication = Publication("./Description.ini")
    print(publication.animal.sexe)