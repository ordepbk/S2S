from typing import Optional
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

    def _get_latests_setlist_data(self, artist_mbid: str) -> Optional[dict]:
        data = self._get(
            endpoint = "/search/setlists",
            params = {
                "artistMbid": artist_mbid,
                "p": 1,
            }
        )

        setlists = data.get("setlist", [])
        if not setlists:
            return None

        return setlists[0]

    def get_setlist(self, artist_name: str):

        artist_mbid = self._get_artist_mbid(artist_name)
        if not artist_mbid:
            return None

        artist_setlist = self._get_latests_setlist_data(artist_mbid)
        if not artist_setlist:
            return None

        sets_container = artist_setlist.get("sets", {})
        sets = sets_container.get("set", [])

        setlist: list[str] = []

        for songs_container in sets:
            songs = songs_container.get("song", [])
            if songs:
                for song in songs:
                    song_name = song.get("name", '')
                    if song_name:
                        setlist.append(song.get("name",''))

        return setlist