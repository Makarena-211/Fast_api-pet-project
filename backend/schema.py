from pydantic import BaseModel
from uuid import UUID

class PaintingBase(BaseModel):
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


class PaintingResponse(PaintingBase):
    id: UUID
    class Config:
        orm_mode = True

