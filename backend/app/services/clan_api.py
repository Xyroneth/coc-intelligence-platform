import os
import requests

API_TOKEN = os.getenv("CLASH_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}


def get_clan(clan_tag: str):
    """
    Fetch clan data from the Clash of Clans API.
    """

    # Remove any leading # and add URL-encoded version
    clan_tag = "%23" + clan_tag.replace("#", "")

    url = f"https://api.clashofclans.com/v1/clans/{clan_tag}"

    response = requests.get(
        url,
        headers=HEADERS
    )

    data = response.json()

    print("\n================ CLAN DEBUG =================")
    print("STATUS:", response.status_code)

    if response.status_code == 200:
        print("Clan Name:", data.get("name"))
        print("Clan Tag:", data.get("tag"))
        print("Clan Level:", data.get("clanLevel"))
        print("Members:", data.get("members"))
        print("War Wins:", data.get("warWins"))
        print("Description:", data.get("description"))

        if "memberList" in data and len(data["memberList"]) > 0:
            print("\n========== FIRST MEMBER ==========")
            print(data["memberList"][0])

    else:
        print("ERROR RESPONSE:")
        print(data)

    print("=============================================\n")

    return data