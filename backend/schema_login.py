from pydantic import BaseModel
class Person(BaseModel):
    id: int
    name: str
    password: str
    sex: str
    role: str

    class Config:
        orm_mode = True

  
class CreatePerson(Person):
    class Config:
        orm_mode = True