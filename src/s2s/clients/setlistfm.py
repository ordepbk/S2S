from s2s.config.settings import settings
import httpx
import json

base_url = "https://api.setlist.fm/rest/1.0/"


def get_artist_mbid(artist_name: str, page: int = 1):
    headers = {"Accept": "application/json", "x-api-key": settings.SETLISTFM_API_KEY}
    endpoint = "search/artists"
    parameters = {"artistName": artist_name, "p": page, "sort": "sortName"}

    response = httpx.get(base_url + endpoint, params=parameters, headers=headers)

    return json.dumps(response.json(), indent=4)


def test():
    artist_name = input("Artist name: ")

    response = get_artist_mbid(artist_name)

    print(response)


if __name__ == "__main__":
    test()
