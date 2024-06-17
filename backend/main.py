from fastapi import FastAPI
import login
import database
import database_login
from config import engine

import paintings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

database.Base.metadata.create_all(bind=engine)
database_login.Base.metadata.create_all(bind=engine)
app.include_router(paintings.router)
app.include_router(login.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3000/login", "http://localhost:3000/create"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"])



