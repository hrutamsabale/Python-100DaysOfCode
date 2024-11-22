import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import spotipy

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

date = input("Enter to a date to travel to (YYYY-MM-DD): ")

with requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}", headers=header) as response:
    content = response.text

soup = BeautifulSoup(content, "html.parser")

all_songs = soup.select("li #title-of-a-story")

songs = []

for song in all_songs:
    songs.append(song.getText().strip())

for song in songs:
    print(song)


