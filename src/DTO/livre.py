class Livre:
    """Representation d'un livre."""
    titre:str
    auteur:str
    description:str
    isbn:str


    def __init__(self, titre:str, auteur:str="", description:str="", isbn:str="" ):
        self.titre = titre
        self.auteur = auteur
        self.description = description
        self.isbn = isbn

    def __str__(self) -> str:
        s = "{titre:" + self.titre + ",auteur:" + self.auteur + ",description:" + self.description + ",isbn:"+ self.isbn + "}"
        return s # self.__dict__()


if __name__ == '__main__':
    livre = Livre("Harry potter", "JK ROWLING")
    print(livre)    

