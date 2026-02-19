from s2s.config.settings import settings
from s2s.clients.setlistfm.client import SetlistFMClient
from s2s.clients.spotify.client import main as sm

def test_setlist():

    client = SetlistFMClient(settings.SETLISTFM_API_KEY)

    artist_name = "parkway drive"  # input("artista: ").strip()


    setlist = client.get_setlist(artist_name)

    if setlist:
        print(f"Artist setlist: {setlist}")
    else:
        print(f"Artist not found")

def test_spotify():
    sm()

def main():
    test_spotify()

if __name__ == "__main__":
    main()
