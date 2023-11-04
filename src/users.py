from pydantic import BaseModel
from bibliotheque import Bibliotheque


class User(BaseModel):
    pseudo:str
    password:str

class Users(BaseModel):
    users:list[User]

    def add_user(self, user:User):
        self.users.append(user)

    def get_user_by_pseudo(self, pseudo:str)-> User:
        for user in self.users:
            if user.pseudo == pseudo:
                return user           
        return None