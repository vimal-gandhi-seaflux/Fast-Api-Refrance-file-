# import datetime
# import email
from os import name
from sqlite3 import Timestamp
from pydantic import BaseModel
from typing import List,Optional

class register(BaseModel):
    name:str
    email:str
    password:str
    createdAt=Timestamp
    class config():
        orm_mode=True

class   login(BaseModel):
    email:str
    password:str

class upload(BaseModel):
    name:str
    email:str
    password:str
    class config():
        orm_mode=True

class update(BaseModel):
    name:str
    numbers:str
    class config:
        orm_mode=True
    class Config():
        arbitrary_types_allowed = True
        
class campain(BaseModel):
    sms_day:str
    status:str
    class config():
        orm_mode=True
        
class camupdate(BaseModel):
    status:str
    class config():
        orm_mode=True  
    class Config():
        arbitrary_types_allowed = True
        
class text(BaseModel):
    text:str  
    createdAt=Timestamp
    updatedAt=Timestamp
    class config():
        orm_mode=True      

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []