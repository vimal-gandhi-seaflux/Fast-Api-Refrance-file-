from datetime import datetime
from anyio import current_time
from fastapi import APIRouter,Depends, Response,status,HTTPException,UploadFile,File
from typing import List
from numpy import number
from sqlalchemy import column
from sqlalchemy.orm import Session
from models import text_table ,number_table ,send_message ,sms_table
from select import select
from database import get_db 

router=APIRouter(
    tags=['send message']
)

@router.get('/')
def send_sms(db:Session = Depends(get_db)):
    user_array=db.execute(number_table.select().with_only_columns(number_table.c.id).limit(5)).fetchall()
    # name=db.execute(number_table.select().with_only_columns(number_table.c.name).limit(5)).fetchall()
    # text =db.execute(text_table.select().with_only_columns(text_table.c.text).limit(5)).fetchall()
    # name=db.execute(number_table.select().with_only_columns(number_table.c.name).limit(5))
    for user in user_array: 
        data = db.execute(text_table.insert().values(
            userid=user.id,
            text="Hello World",     
            createdAt =datetime.now(),
        ))
    db.commit()
    return {
        "message": "SMS sent successfully."
    }
    
            
        


        
        
        
    
    




