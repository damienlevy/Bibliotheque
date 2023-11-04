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
    proprietaire: Créateur et proprietaire de la bibliothèque
    """
    nom: str
    list_livres: list[Livre]
    zone: Zone
    prorietaire:User

    def _list_to_string(self) -> str:
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
    """Représentation d'une liste de bibliothèque accessible par un utilisateur
    Attribut
    --------
    user: utilisateur
    liste_biblio: Liste des bibliothèques accessible à l'utilisateur
    """
    user:User
    liste_biblio: list[Bibliotheque]

    def add_bibliotheque(self, biblio:Bibliotheque):
        self.liste_biblio.append(biblio)
    
