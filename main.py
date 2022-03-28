from fastapi import FastAPI
from routers import operation,register,upload,getdata,sms,text,send_message,days_fatch
import models 
from database import engine

app=FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(register.router)
app.include_router(operation.router)
app.include_router(upload.router)
app.include_router(getdata.router)
app.include_router(sms.router)
app.include_router(text.router)
app.include_router(send_message.router)
app.include_router(days_fatch.router)


