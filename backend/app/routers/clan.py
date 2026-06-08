from fastapi import APIRouter
from app.services.clan_api import get_clan

router = APIRouter()

@router.get("/clan/{clan_tag}")
def clan_info(clan_tag: str):
    return get_clan(clan_tag)