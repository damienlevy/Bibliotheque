from pydantic import BaseModel
from bibliotheque import Bibliotheque


class User(BaseModel):
    pseudo:str
    password:str
    # list_bibliotheque: list[Bibliotheque]

    # def __init__(self, pseudo:str, password:str) -> None:
    #     self.pseudo = pseudo
    #     self.password = password
    #     self.list_bibliotheque = list()
    

class Users(BaseModel):
    users:list[User]

    def add_user(self, user:User):
        self.users.append(user)

    def get_user_by_pseudo(self, pseudo:str)-> User:
        for user in self.users:
            if user.pseudo == pseudo:
                return user           
        return None