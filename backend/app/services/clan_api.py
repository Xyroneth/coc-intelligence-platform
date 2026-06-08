import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("CLASH_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_clan(clan_tag: str):
    clan_tag = "%23" + clan_tag.replace("#", "")

    url = f"https://api.clashofclans.com/v1/clans/{clan_tag}"

    response = requests.get(
        url,
        headers=HEADERS
    )

    print("CLAN STATUS:", response.status_code)

    return response.json()