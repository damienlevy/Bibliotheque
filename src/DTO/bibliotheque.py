from DTO.livre import Livre
from DTO.zone import Zone


class Bibliotheque:
    nom: str
    list_livres: list[Livre]
    zone: Zone

    def __init__(self, nom: str, list_livres:list[Livre]|None, zone:Zone|None) -> None:
        self.nom = nom
        self.list_livres = list_livres
        self.zone = zone

    def list_to_string(self) -> str:
        s = "["
        for livre in self.list_livres:
            s += str(livre)
            s += "," if len(self.list_livres) > 1 else ""
        s = s[:-1]
        s += "]"
        return s

    def __str__(self) -> str:
        livres = self.list_to_string()
        return "{nom:" + self.nom + ",livres:" + livres + ",zone:" + str(self.zone) + "}"