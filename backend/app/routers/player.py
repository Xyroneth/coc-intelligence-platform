from fastapi import APIRouter
from app.services.clash_api import get_player

router = APIRouter()

@router.get("/player/{player_tag}")
def player_info(player_tag: str):
    return get_player(player_tag)