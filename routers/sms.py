from fastapi import APIRouter,Depends, Response,status ,HTTPException
from numpy import insert
from sqlalchemy.orm import Session
import  schemas
from datetime import datetime
from models import sms_table ,text_table
from sqlalchemy import column
from database import get_db
router=APIRouter(tags=['campain'] )

#only edit

@router.post('/camp')
def register(response:Response,request:schemas.campain,db:Session=Depends(get_db)):
    data = db.execute(sms_table.insert().values(sms_day=request.sms_day,status=request.status,createdAt=datetime.now()))
    db.commit()
    return 'added'


    
@router.get('/camp')
def all(db:Session=Depends(get_db)):
    user = db.query(sms_table).all()
    return user


@router.put('/',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.camupdate,db:Session=Depends(get_db)):
    blog=db.query(sms_table).filter(sms_table.c.id==id,UpdatedAt=datetime.now())
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with {id} not here")
    blog.update(request.dict())
    db.commit()
    db.refresh()
    return "updated"





