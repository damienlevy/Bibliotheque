from fastapi import FastAPI, Request
from fastapi.responses import Response, StreamingResponse
from fastapi.templating import Jinja2Templates
from typing import List

from users import User, Users
from bibliotheque import Bibliotheque, Livre, Zone


app = FastAPI()

mock_books = [Livre(titre="Les misérable",auteur="HUGO Victor"), Livre(titre="Harry Potter à l'école des sorcier",auteur="J.K.Rowling"), Livre(titre="Harry Potter et la chambre des secrets",auteur="J.K.Rowling")]
mock_zones = [Zone(nom_zone="Escalier"), Zone(nom_zone="Salon"), Zone(nom_zone="Cuisine")]
user = User(pseudo="admin",password="admin",list_bibliotheque=[Bibliotheque(nom="admin",list_livres=mock_books,zone=mock_zones[0])])
users_temp = Users(users=[user])

templates = Jinja2Templates(directory="")


@app.get("/livres")
def get_books():
    """Retourne l'ensembles des livres présent dans la bibliothèque"""
    return mock_books

@app.get("/zones")
def get_zones():
    """Retourne l'ensembles des zones existantes dans la bibliothèque"""
    return mock_zones

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/users')
def get_user():
    return users_temp

@app.post('/user')
def new_user(user:User):
    users_temp.add_user(user=user)
    return user