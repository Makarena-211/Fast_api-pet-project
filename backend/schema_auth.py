from pydantic import BaseModel
class Person(BaseModel):
    name: str
    last_name: str
    email: str
    role: str
    password: str
    

    class Config:
        orm_mode = True

  
class CreatePerson(Person):
    class Config:
        orm_mode = True
 
    