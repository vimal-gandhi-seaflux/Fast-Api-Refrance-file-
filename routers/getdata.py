from ast import Str
from pyexpat import model
from select import select
from fastapi import APIRouter,Depends, Response,status,HTTPException
from numpy import where
from sqlalchemy.orm import Session
from database import  get_db
import database 
from models import number_table 

router=APIRouter(
    tags=['camp'] 
    )

@router.get('/{page_no}/{numberdata}')
def getNumber(numberdata:int,page_no:int,db:Session = Depends (database.get_db)):
    data=db.execute(number_table.select().limit(numberdata).offset(page_no*50)).fetchall()    
    return data

