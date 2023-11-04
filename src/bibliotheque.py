from pydantic import BaseModel

from users import User, Users

class Livre(BaseModel):
    """Representation d'un livre.
    Attribut
    --------
    titre: Titre du livre
    auteur: Auteur du livre
    isbn: isbn du livre
    """
    titre:str
    auteur:str
    description:str | None
    isbn:str | None

    def __str__(self) -> str:
        s = "{titre:" + self.titre + ",auteur:" + self.auteur + ",description:" + self.description + ",isbn:"+ self.isbn + "}"
        return s # self.__dict__()

class Zone(BaseModel):
    """Representation d'une zone.
    Attribut
    --------
    nom_zone: nom de la zone (par exemple : bureau, couloir...)
    """
    nom_zone:str

    def __str__(self) -> str:
        return "{0}".format(self.nom_zone)

class Bibliotheque(BaseModel):
    """Representation d'une bibliothèque.
    Attribut
    --------
    nom: Nom de la bibliothèque
    list_livres: Liste des livres présent dans la bibliothèque
    zone: Zone ou se trouve la bibliothèque
    """
    nom: str
    list_livres: list[Livre]
    zone: Zone

    # def __init__(self, nom: str, list_livres:list[Livre]|None, zone:Zone|None) -> None:
    #     self.nom = nom.title()
    #     self.list_livres = list_livres
    #     self.zone = zone

    def list_to_string(self) -> str:
        s = "["
        for livre in self.list_livres:
            s += str(livre)
            s += "," if len(self.list_livres) > 1 else ""
        # s = s[:-1]
        s += "]"
        return s

    def __str__(self) -> str:
        livres = self.list_to_string()
        return "{nom:" + self.nom + ",livres:" + livres + ",zone:" + str(self.zone) + "}"
    
    def get_livre_by_title(self, title:str) -> Livre:
        for livre in self.list_livres:
            if livre.titre == title.title():
                return livre
        return None
    
    def get_livre_by_auteur(self, auteur:str) -> list[Livre]:
        return [l for l in self.list_livres if l.auteur==auteur.title()]

    def add_livre(self, livre: Livre):
        self.list_livres.append(livre)
    
    def add_livres(self, livres: list[Livre]):
        self.list_livres.extend(livres)
    
    def remove_livre_by_title(self, titre:str):
        self.list_livres.remove(self.get_livre_by_title(titre))


class Bibliotheques(BaseModel):
    """Représentation d'une liste de bibliothèque créée par un utilisateur
    Attribut
    --------
    proprietaire: Créateur et proprietaire des bibliothèques
    liste_biblio: Liste des bibliothèques appartenant à un user
    """
    prorietaire:User
    liste_biblio: list[Bibliotheque]

if __name__ == '__main__':
    harry_potter = Livre("Harry potter", "JK ROWLING")
    ne_le_dis_a_personne = Livre("Ne le dis à personne", "Harlan Koben")
    titeuf = Livre("Titeuf","ZEP")
    livres = [harry_potter,ne_le_dis_a_personne]
    bibliotheque = Bibliotheque("test",livres,Zone("bureau"))
    print(bibliotheque)
    bibliotheque.add_livre(titeuf)
    print("add titeuf : ")
    print(bibliotheque)
    bibliotheque.remove_livre_by_title("Titeuf")
    print("remove titeuf")
    print(bibliotheque)
    list_harlan_coben = bibliotheque.get_livre_by_auteur("harlan Koben")
    for livre in list_harlan_coben:
        print(livre)
    bibliotheque2 = Bibliotheque("test2",[],Zone("chambre"))
    bibliotheque2.add_livres(list_harlan_coben)
    print(bibliotheque2)