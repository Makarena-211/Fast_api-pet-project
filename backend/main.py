from fastapi import FastAPI
from pydantic import BaseModel
import database
from config import engine
import paintings
app = FastAPI()

database.Base.metadata.create_all(bind=engine)
app.include_router(paintings.router)



@app.get('/')
async def main():
    return 'hello world'
