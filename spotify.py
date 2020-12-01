from urllib.parse import urlencode
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv('.env')


class Spotify: 
    scope = 'playlist-modify-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user = sp.current_user()['id']

    def search_song(self, name , artist):
        results = self.sp.search(f'{name} {artist}', type='track')
        try: 
            song_uri = results['tracks']['items'][0]['uri']
            return song_uri
        except: 
            return None

    def search_songs(self, songs): 
        song_uris = []
        print('Searching songs on Spotify\n')
        for song in tqdm(songs): 
            _, name, artist = song
            song_uri = self.search_song(name, artist) 
            if song_uri: 
                song_uris.append(song_uri)

        print(f'Found {len(song_uris)}/100 songs')
        self.song_uris = song_uris

    def create_playlist(self, date): 
        playlist_name = f'{date} Billboard 100'
        print(f'Creating playlist named {playlist_name}')
        playlist = self.sp.user_playlist_create(self.user, playlist_name, public=False)
        self.playlist_url = playlist['external_urls']['spotify']
        self.playlist_id = playlist['id']
    
    def add_songs_to_playlist(self): 
        print('Adding songs to playlist')
        self.sp.playlist_add_items(self.playlist_id, self.song_uris)
        print('DONE!!!')
        print(f'Playlist URL: {self.playlist_url}')