from fastapi import FastAPI
from pydantic import BaseModel
class Painting(BaseModel):
    id: int
    name: str
    photo: str
    author: str
    price: int
    type: str
app = FastAPI()

data = {'id': 0, 'name':'evening', 'paint':'sdofgodfgndofg', 'author':'Victoria', 'price':245532}
@app.get('/')
async def main(data):
    return data
