from base64 import b64encode
import urllib.parse

import httpx
from s2s.clients.spotify.schemas import ExchangeCodeResponse
from s2s.config.settings import settings


AUTH_URL = "https://accounts.spotify.com/authorize?"
TOKEN_URL = "https://accounts.spotify.com/api/token?"
SCOPES = ["playlist-modify-public", "playlist-modify-private"]

BYTES_CLIENT_ID = settings.SPOTIFY_CLIENT_ID.encode("utf-8")
BYTES_CLIENT_SECRET = settings.SPOTIFY_CLIENT_SECRET.encode("utf-8")


class SpotifyAuth:
    @staticmethod
    def get_auth_code(state: str) -> ...:
        params = {
            "response_type": "code",
            "client_id": settings.SPOTIFY_CLIENT_ID,
            "scope": SCOPES,
            "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
            "state": state,
        }

        return f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    @staticmethod
    async def exchange_code_for_token(code: str) -> ExchangeCodeResponse:

        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {b64encode(BYTES_CLIENT_ID)}:{b64encode(BYTES_CLIENT_SECRET)}",
        }

        params = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        }

        response = httpx.get(TOKEN_URL, headers=header, params=params)
        response.raise_for_status()

        parsed_data = ExchangeCodeResponse.model_validate(response.json())

        return parsed_data

    @staticmethod
    async def update_token(refresh_token: str) -> ExchangeCodeResponse:
        header = {
            "content-type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {b64encode(BYTES_CLIENT_ID)}:{b64encode(BYTES_CLIENT_SECRET)}",
        }

        params = {"grant_type": "refresh_token", "code": refresh_token}

        response = httpx.put(TOKEN_URL, headers=header, params=params)
        response.raise_for_status()

        parsed_data = ExchangeCodeResponse.model_validate(response.json())

        return parsed_data
