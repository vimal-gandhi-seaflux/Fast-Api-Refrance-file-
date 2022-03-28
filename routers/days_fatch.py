from datetime import  datetime, timedelta
from fastapi import APIRouter,Depends, Response,status,HTTPException,UploadFile,File
from typing import List
from numpy import number
from sqlalchemy import column
from sqlalchemy.orm import Session
from models import text_table ,number_table ,send_message ,sms_table
from select import select
from database import get_db 

router=APIRouter(tags=['Dashboard'])

@router.get('/day_fetch')
def Deshbord(db:Session = Depends(get_db)):
    # count_number = db.execute(send_message.select().with_only_columns(send_message.c.number)).fetchall()
    # n=0
    # for i in count_number:
    #     N = n + 1
    v= '0' 
    for x in range(7):
        d = datetime.now() - timedelta(days=x)
        send_message_number = db.execute(send_message.select().where(send_message.c.createdAt == datetime.now())).fetchall()         
        # date =(d.strftime("%Y-%m-%d") +  f' send number {send_message_number[0][0]}')
        # return date
        print(send_message_number)
        return send_message_number
    #     v = date + v 
    #     db.commit()              
    # return v
        
        
        
   


   
    