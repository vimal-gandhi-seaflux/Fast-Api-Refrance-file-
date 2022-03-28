# from fastapi import APIRouter, File, UploadFile,Depends
# from sqlalchemy import Date
# from sqlalchemy.orm import Session
# from io import StringIO
# from datetime import datetime
# import models
# import pandas as pd
# from database import get_db
# router= APIRouter()

# @router.post("/uploadfile/" , tags=['Upload'])
# async def create_upload_file(file: UploadFile = File(...),db:Session=Depends(get_db)):  
#     data=pd.read_csv(StringIO(str(file.file.read(), "UTF-8")), encoding="UTF-8")
#     for index in range(len(data.index)):
#         name=f'{data.iloc[index][0]}{data.iloc[index][1]}'
#         num=str(data.iloc[index][2])
#         new=db.execute(models.number_table.insert().values(
#             name=name,
#             number=num,
#             createdAt=datetime.now()
#             ))
#         db.commit()  
#     return 'updated'