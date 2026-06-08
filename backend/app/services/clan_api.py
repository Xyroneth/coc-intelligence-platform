import os
import requests

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

    data = response.json()

    print("\n==================== CLAN DEBUG ====================")
    print("STATUS:", response.status_code)
    print("Clan Name:", data.get("name"))
    print("Clan Tag:", data.get("tag"))
    print("Clan Level:", data.get("clanLevel"))
    print("Members:", data.get("members"))
    print("War Wins:", data.get("warWins"))
    print("Description:", data.get("description"))
    print("====================================================\n")

    return data