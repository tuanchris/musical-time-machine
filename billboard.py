import requests
from bs4 import BeautifulSoup
import datetime

class BillBoard: 
    endpoint = 'https://www.billboard.com/charts/hot-100/{}'

    def __init__(self, date='2000-08-12') -> None:
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

        self.endpoint = self.endpoint.format(date)

    def request_website(self): 
        response = requests.get(self.endpoint)
        self.payload = response.text
    
    def get_data(self): 
        print('Getting data from billboard\n')
        self.soup = BeautifulSoup(self.payload, 'html.parser') 

    def parse_data(self): 
        print('Parsing data from billboard\n')
        soup = self.soup

        songs_obj = soup.find_all('span', class_= 'chart-element__information__song')
        songs = [song_obj.get_text() for song_obj in songs_obj]

        artists_obj = soup.find_all('span', class_='chart-element__information__artist')
        artists = [artist_obj.get_text() for artist_obj in artists_obj]

        ranks_obj = soup.find_all('span', class_='chart-element__rank__number')
        ranks = [rank_obj.get_text() for rank_obj in ranks_obj]

        return list(zip(ranks, songs, artists))
