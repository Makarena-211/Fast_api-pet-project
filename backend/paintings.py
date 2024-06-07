from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
import database
from fastapi import APIRouter
from config import get_db
import schema
from uuid import UUID
router = APIRouter(
    prefix = '/paintings',
    tags=['Paintings']
)

@router.get('/', response_model=List[schema.PaintingResponse])
def test_paintings(db: Session=Depends(get_db)):
    painting = db.query(database.Painting).all()
    return painting

@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=schema.PaintingResponse)
def create_paintings(painting_create: schema.CreatePainting, db: Session = Depends(get_db)):
    new_painting = database.Painting(**painting_create.dict())
    db.add(new_painting)
    db.commit()
    db.refresh(new_painting)
    return new_painting

@router.delete('/delete/{painting_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_paintings(painting_id: UUID, db: Session = Depends(get_db)):
    painting = db.query(database.Painting).filter(database.Painting.id == painting_id).first()
    if painting is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Painting not found")
    db.delete(painting)
    db.commit()
    return db

@router.get('/{id}', response_model=schema.PaintingResponse, status_code=status.HTTP_200_OK)
def get_by_id(painting_id: int, db:Session = Depends(get_db)):
    painting = db.query(database.Painting).filter(database.Painting.id == painting_id).first()
    if painting is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"NO!")
    return painting

@router.put('/update/{painting_id}', response_model=schema.PaintingResponse)
def update_painting(update_painting: schema.PaintingBase, painting_id: UUID, db: Session = Depends(get_db)):
    updated_painting = db.query(database.Painting).filter(database.Painting.id == painting_id)
    updated_painting.update(update_painting.dict(), synchronize_session=False)
    db.commit()
    
    return updated_painting.first()
