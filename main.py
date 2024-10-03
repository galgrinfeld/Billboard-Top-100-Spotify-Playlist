import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

answer = input("what year would you  like to travel to in YYYY-MM-DD format: ")
URL = f"https://www.billboard.com/charts/hot-100/{answer}"

USER_NAME = "31z4gstq2xt3hmmigzh7xvj6u5di"


CLIENT_ID = "ba8c713e8bab482db9cdbecc09507856"
CLIENT_SECRET = "f603d18499cf4681b063d0a9fe36bbcd"
URI = "http://example.com"



response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = []
for song in song_names_spans:
    song_names.append(song.getText().strip())

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        cache_path="token.txt",

    )
)
User_id = sp.current_user()["id"]
song_uris = []
year = answer.split('-')[0]
for song in song_names:
  result = sp.search(q=f"track:{song} year:{year}", type="track")
  try:
    uri = result["tracks"]["items"][0]["uri"]
  except IndexError:
    pass
  else:
    song_uris.append(uri)

top_100 = sp.user_playlist_create(user=User_id, name=f"{answer} Billboard 100", public=True)
sp.playlist_add_items(playlist_id=top_100["id"], items=song_uris)
print(f"https://open.spotify.com/playlist/{top_100['id']}")
