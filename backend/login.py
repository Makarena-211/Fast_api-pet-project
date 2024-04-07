from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from database_login
from fastapi import APIRouter
from config import get_db
import schema_login

router = APIRouter(
    prefix = '/login',
    tags=['Login']
)

@router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=List[schema_login.CreatePerson])
def create_user(person_create: schema_login.CreatePerson, db: Session = Depends(get_db)):
    new_person = database_login.Person(**person_create.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person


@router.post("/authenticate_user", response_model=List[schema_login.Person])
def authenticate_user(person: schema_login.Person, db: Session = Depends(get_db)):
    person = db.query(person).filterby(person = person.name, password = person.password, role = person.role).first()
    if not person:
        return None
    return person