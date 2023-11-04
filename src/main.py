from bibliotheque import Bibliotheque, Zone, Livre


if __name__ == '__main__':
    zone = Zone("Maison")
    book = Livre(titre="Identités croisées",auteur="Harlan Coben",isbn="978-2-7144-9509-9")
    book2 = Livre(titre="Harry Potter à l'école des sorciers",auteur="JK Rowling")
    bibliotheque = Bibliotheque("Bibliothèque de Test", list_livres=[book,book2], zone=zone)
    print(bibliotheque)
    