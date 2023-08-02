from fastapi import FastAPI, Request
from fastapi.responses import Response, StreamingResponse
from typing import List
from DTO.livre import Livre
from DTO.zone import Zone
import cv2
import json
from fastapi.templating import Jinja2Templates

app = FastAPI()

mock_books = [Livre("Les misérable","HUGO Victor"), Livre("Harry Potter à l'école des sorcier","J.K.Rowling"), Livre("Harry Potter et la chambre des secrets","J.K.Rowling")]
mock_zones = [Zone("Escalier"), Zone("Salon"), Zone("Cuisine")]

templates = Jinja2Templates(directory="")


@app.get("/livres")
def get_books():
    """Retourne l'ensembles des livres présent dans la bibliothèque"""
    return mock_books

@app.get("/zones")
def get_zones():
    """Retounre l'ensembles des zones existantes dans la bibliothèque"""
    return mock_zones

# cam = cv2.VideoCapture(0)
# 
# @app.get("/cam")
# def get_cam():
#     def iter_cam():
#         while True:
#             ret, image = cam.read()
#             
#             if(ret):
#                 _, buffer = cv2.imencode('.jpg', image)
#                 frame = buffer.tobytes()
#                 yield (b'--frame\r\n' 
#                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#             else:
#                 print("coucou")
#     # ret, image = cam.read()
#     # print("image : {0}".format(image))
#     return StreamingResponse(iter_cam(), media_type='multipart/x-mixed-replace; boundary=frame')

# @app.get('/')
# def index(request: Request):
#     return templates.TemplateResponse("test.html", {"request": request})

# @app.get('/')
# def index():
#     return Response(status_code=200)

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
