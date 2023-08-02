class Zone:

    def __init__(self, nom_zone:str) -> None:
        self.nom_zone = nom_zone

    def __str__(self) -> str:
        return "{0}".format(self.nom_zone)