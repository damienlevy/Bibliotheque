from fastapi import FastAPI
from typing import List
from DTO.livre import Livre
from DTO.zone import Zone

app = FastAPI()

mock_books = [Livre("Les misérable","HUGO Victor"), Livre("Harry Potter à l'école des sorcier","J.K.Rowling"), Livre("Harry Potter et la chambre des secrets","J.K.Rowling")]
mock_zones = [Zone("Escalier"), Zone("Salon"), Zone("Cuisine")]

@app.get("/livres")
def get_books():
    """Retourne l'ensembles des livres présent dans la bibliothèque"""
    return mock_books

@app.get("/zones")
def get_zones():
    """Retounre l'ensembles des zones existantes dans la bibliothèque"""
    return mock_zones
