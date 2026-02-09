from typing import Any, List
import httpx

BASE_URL = "https://api.setlist.fm/rest/1.0/"


class SetlistFMClient:

    def __init__(self, api_key: str):
        self.headers = {
            "Accept": "application/json",
            "x-api-key": api_key,
        }

    def _get_artist(self, artist_name: str, page: int = 1):
        url = f"{BASE_URL}search/artists"
        parameters = {
            "artistName": artist_name,
            "p": page,
            "sort": "sortName",
            "timeout": 10,
        }

        response = httpx.get(url, params=parameters, headers=self.headers)
        response.raise_for_status()

        return response.json()

    def _get_mbid(self, artist_name: str):
        data = self._get_artist(artist_name)
        artist = data.get("artist", None)[0]

        if not artist:
            return None

        return artist.get("mbid")

    def _get_setlist_data(self, artist_name: str, page: int = 1):
        url = f"{BASE_URL}search/setlists"
        artist_mbid = self._get_mbid(artist_name)

        parameters = {
            "artistMbid": artist_mbid,
            "p": page,
            "timeout": 10,
        }

        response = httpx.get(url, params=parameters, headers=self.headers)
        response.raise_for_status()

        return response.json()

    def _get_setlist(self, artist_name: str):
        setlist = []
        data = self._get_setlist_data(artist_name)
        setlist_data = data.get("setlist", [])[0]

        if not setlist_data:
            return None

        sets = setlist_data.get("sets", [])

        if not sets:
            return None

        set = sets.get("set", [])

        for group in set:
            songs = group.get("song", [])

            if not songs:
                return None

            for song in songs:
                song_name = song.get("name", "")

                if not song_name:
                    return None

                setlist.append(song_name)

        return setlist
