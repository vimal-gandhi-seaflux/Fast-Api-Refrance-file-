from fastapi import APIRouter,Depends, Response,status,HTTPException,UploadFile,File
from typing import List
from sqlalchemy import column
from sqlalchemy.orm import Session
import models,schemas
from datetime import datetime
from routers import hashing
from routers.token import create_access_token,timedelta
from database import get_db 

router=APIRouter(
    tags=['authentication']
)

@router.post('/register')
def register(response:Response,request:schemas.register,db:Session=Depends(get_db)):
    new_data = db.execute(models.user.insert().values(name=request.name,email=request.name,createdAt=datetime.now(),password =hashing.hash.bcrypt(request.password)))
    db.commit()
    return 'succesfull'

@router.post("/login")
def login(request:schemas.login,db:Session=Depends(get_db)):
    user=db.query(models.user).filter(models.user.email==request.email).first()
    if not user:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid  ")
    if not hashing.hash.verify(request.password,user.password,):
        raise  HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
