from sqlalchemy import Column,Table , Integer,String ,ForeignKey
from database import Base 
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship

user=Table(
        "user",
        Base.metadata,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("name",String),
        Column("numbers",Integer),
        Column('email',String),
        Column('password',String),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime)
                )    
    
    
number_table=Table(
        "number",
        Base.metadata,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("name",String),
        Column("numbers",Integer),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime)
                  )

sms_table=Table(
        "sms",
        Base.metadata,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("userid",String),
        Column("sms_day",Integer),
        Column("status",String),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime),
               )   
text_table=Table(
        "text",
        Base.metadata,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("text",String),
        Column("userid",Integer),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime),
        )       
       
send_message=Table(
        "send_messages",
        Base.metadata,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("number",Integer),
        Column("text",String),
        Column("name",String),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime),
        )   
 