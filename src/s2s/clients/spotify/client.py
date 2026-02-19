import json
import httpx
from s2s.config.settings import settings
TOKEN_URL = "https://accounts.spotify.com/api/token"


def main():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    params = {
        "grant_type": "client_credentials",
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "client_secret": settings.SPOTIFY_CLIENT_SECRET
    }

    response = httpx.post(TOKEN_URL, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    access_token = data.get("access_token", '')
    print(access_token)

