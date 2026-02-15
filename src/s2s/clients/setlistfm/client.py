from typing import List, Optional
from s2s.clients.setlistfm.schemas import SetlistSearchResponse
import httpx

BASE_URL = "https://api.setlist.fm/rest/1.0"


class SetlistFMClient:

    def __init__(self, api_key: str) -> None:
        self._client = httpx.Client(
            base_url=BASE_URL,
            headers = {
                "Accept": "application/json",
                "x-api-key": api_key,
            },
            timeout=10.0
        )

    def _get(self, endpoint: str, params: dict) -> dict:
        response = self._client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def _get_artist_mbid(self, artist_name: str) -> Optional[str]:
        data = self._get(
            endpoint = "/search/artists",
            params = {
                "artistName": artist_name,
                "p": 1,
                "sort": "sortName",
            }
        )

        artists = data.get("artist", [])

        if not artists:
            return None

        return artists[0].get("mbid")

    def _fetch_setlist_data(self, artist_mbid: str) -> Optional[SetlistSearchResponse]:
        raw_data = self._get(
            endpoint="/search/setlists",
            params={
                "artistMbid": artist_mbid,
                "p": 1,
            }
        )

        parsed = SetlistSearchResponse.model_validate(raw_data)
        return parsed if parsed.setlist else None

    def _extract_songs(self, parsed: SetlistSearchResponse) -> List[str]:
        first_setlist = parsed.setlist[0]
        return [
            song.name
            for set in first_setlist.sets.set
            for song in set.song
        ]

    def get_setlist(self, artist_name: str) -> Optional[List[str]]:
        artist_mbid = self._get_artist_mbid(artist_name)
        if not artist_mbid:
            return None

        parsed = self._fetch_setlist_data(artist_mbid)
        if not parsed:
            return None

        return self._extract_songs(parsed)

