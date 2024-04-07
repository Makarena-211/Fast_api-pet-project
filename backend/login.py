from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
import database_login
from fastapi import APIRouter
from config import get_db
import schema_login

router = APIRouter(
    prefix = '/login',
    tags=['Login']
)

@router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=schema_login.CreatePerson)
def create_user(person_create: schema_login.CreatePerson, db: Session = Depends(get_db)):
    new_person = database_login.Person(**person_create.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person


@router.post("/authenticate_user", response_model=schema_login.Person)
def authenticate_user(person:schema_login.Person, db: Session = Depends(get_db)):
    user = db.query(database_login.Person).filter(database_login.Person.name == person.name, database_login.Person.password == person.password, database_login.Person.role == person.role).first()
    if not user:
        return None
    return user