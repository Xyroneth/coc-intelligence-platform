import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("CLASH_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_player(player_tag: str):
    player_tag = "%23" + player_tag.replace("#", "")

    url = f"https://api.clashofclans.com/v1/players/{player_tag}"

    print("URL:", url)

    response = requests.get(
        url,
        headers=HEADERS
    )

    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    return response.json()