from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.player import router as player_router
from app.routers.clan import router as clan_router

app = FastAPI(title="CoC Intelligence Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(player_router)
app.include_router(clan_router)


@app.get("/")
def home():
    return {"message": "CoC Intelligence Platform Backend Running"}