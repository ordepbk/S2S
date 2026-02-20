import urllib.parse
from s2s.config.settings import settings


AUTH_URL = "https://accounts.spotify.com/authorize?"
SCOPES = ["playlist-modify-public", "playlist-modify-private"]


def generate_auth_url(state: str) -> str:
    params = {
        "response_type": "code",
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "scope": SCOPES,
        "redirect_uri": settings.SPOTIFY_REDIRECT_URI,
        "state": state,
    }

    return f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
