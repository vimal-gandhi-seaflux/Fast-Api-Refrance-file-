from datetime import datetime
from fastapi import APIRouter,Depends, Response
from sqlalchemy.orm import Session
import models,schemas
from database import get_db 
router=APIRouter(
    tags=['Text']
)
@router.post('/')
def register(response:Response,request:schemas.text,db:Session=Depends(get_db)):
    new_user = db.execute(models.text_table.insert().values(text = request.text,createdAt=datetime.now()))
    db.commit()
    return 'new user added'