from billboard import BillBoard
from spotify import Spotify

if __name__ == '__main__': 
    date = input('Which date do you want to travel to? (date format YYYY-MM-DD): ')
    bb = BillBoard(date)
    bb.request_website()
    bb.get_data()
    songs = bb.parse_data()
    
    sp = Spotify()
    sp.search_songs(songs)
    sp.create_playlist(date)
    sp.add_songs_to_playlist()