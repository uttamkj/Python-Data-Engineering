
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException

client_id = '37b559abc84749f88a65d55a5d928676'
client_secret = '212449d155aa4333aa2a1f94ad538cb1'

client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_link = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF'

# strip off any query params (e.g. ?si=...)
playlist_id = playlist_link.split('/')[-1].split('?')[0]

try:
    results = sp.playlist_tracks(playlist_id)
    print(results)
except SpotifyException as exc:
    print(f"Spotify API error: {exc}")
    print("Check your credentials and that the playlist is accessible with your Spotify app subscription.")