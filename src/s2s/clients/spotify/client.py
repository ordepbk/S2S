from typing import Optional

import httpx

BASE_URL = "https://api.spotify.com/v1/me/"


class SpotifyClient:

    def __init__(self, token: str) -> None:
        self._client = httpx.Client(
            base_url=BASE_URL,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            },
            timeout=10.0,
        )

    def _get(self, endpoint: str, params: dict) -> dict:
        response = self._client.get(url=endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def create_new_playlist(
        self, playlist_name: str, playlist_description: str
    ) -> Optional[str]:
        data = self._get(
            endpoint="playlists",
            params={
                "name": playlist_name,
                "description": playlist_description,
                "public": False,
            },
        )

        if not data:
            return None
        # TODO: Check API doc
        return data["playlist_id"]
