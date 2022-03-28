from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models,schemas

router=APIRouter(tags=['Number'] )

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    number =db.execute(models.number_table.select().where(models.number_table.c.id==id)).first()
    if not number:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with {id} not here")
    db.execute(models.number_table.delete().where(models.number_table.c.id==id))
    db.commit()
    return "deteted"



@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.update,db:Session=Depends(get_db)):
    camp=db.query(models.number_table).filter(models.number_table.c.id==id)
    if not camp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with {id} not here")
    camp.update(request.dict())
    db.commit()
    return "updated"
































# @router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
# def update(id,request:schemas.update,db:Session=Depends(get_db)):
#     # number=db.execute(models.user).filter(models.user.id==id)
#     number =db.query(models.number_table.select().where(models.number_table.c.id==id)).first()
#     if not number:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with {id} not here")
#     number.update()
#     db.commit(request.dict())
#     return "updated"

# @router.put("/number")
# def add_number(responce:Response,request:schemas.update,db:Session=Depends(get_db)):
#     new_number= models.number(first_name=request.first_name,last_name=request.last_name,number=request.number,birthday_date=request.birthday_date)
#     db.add(new_number)
#     db.commit()
#     db.refresh(new_number)
#     return new_number