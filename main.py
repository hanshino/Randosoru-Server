from fastapi import FastAPI, Query, Path, Body, HTTPException, Depends
#CORS
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",
    "http://localhost:3000",
]
#
import config
from routes import oauth, user, guild

app = FastAPI()

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#


app.include_router(oauth.router)
app.include_router(user.router)
app.include_router(guild.router)
