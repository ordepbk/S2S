from s2s.config.settings import settings
from s2s.clients.setlistfm import SetlistFMClient

def main():

    client = SetlistFMClient(settings.SETLISTFM_API_KEY)

    artist_name = "parkway drive"  # input("artista: ").strip()


    setlist = client.get_setlist(artist_name)

    if setlist:
        print(f"Artist setlist: {setlist}")
    else:
        print(f"Artist not found")


if __name__ == "__main__":
    main()
