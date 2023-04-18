class Livre:
    """Representation d'un livre."""
    titre:str
    auteur:str
    description:str


    def __init__(self, titre:str, auteur:str="", description:str="" ):
        self.titre = titre
        self.auteur = auteur
        self.description = description

    def __str__(self) -> str:
        return "{\n'titre':" + self.titre +",\n'auteur':" + self.auteur + ",\n'description':" + self.description + "\n}"