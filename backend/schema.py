from pydantic import BaseModel

class PaintingBase(BaseModel):
    id: int
    name: str
    photo: str
    author: str
    price: int
    type: str
    
    class Config:
        orm_mode = True

class CreatePainting(PaintingBase):
    class Config:
        orm_mode = True



