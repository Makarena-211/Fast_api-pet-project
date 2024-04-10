from typing import List
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
import database_login
from fastapi import APIRouter
from config import get_db
import schema_auth
import schema_login
import jwt
from fastapi.encoders import jsonable_encoder

SECRET_KEY = "test"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 800

router = APIRouter(
    prefix = '/login',
    tags=['Login']
)

@router.post("/create_user", status_code=status.HTTP_201_CREATED, response_model=schema_auth.CreatePerson)
def create_user(person_create: schema_auth.CreatePerson, db: Session = Depends(get_db)):
    new_person = database_login.Person(**person_create.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person


@router.post("/authenticate_user")
def authenticate_user(login:schema_login.Login, db: Session = Depends(get_db)):
    user = db.query(database_login.Person).filter(database_login.Person.email == login.email, database_login.Person.password == login.password).first()
    token_data = {'email': user.email, 'role':user.role, 'password':user.password}
    print(token_data)  # Добавьте другие необходимые данные пользователя
    encoded_jwt = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {'token':encoded_jwt} #token = str
    
    
    
    