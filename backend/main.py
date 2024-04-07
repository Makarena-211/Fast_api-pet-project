from fastapi import FastAPI
from pydantic import BaseModel
import database
from config import engine
import paintings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

database.Base.metadata.create_all(bind=engine)
app.include_router(paintings.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get('/')
async def main():
    return 'hello world'
