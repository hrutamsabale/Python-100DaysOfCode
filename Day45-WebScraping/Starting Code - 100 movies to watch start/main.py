import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

with requests.get(url=URL) as response:
    content = response.text

soup = BeautifulSoup(content, "html.parser")

all_titles = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]

all_titles = all_titles[::-1]

with open("./100 Movies To Watch.txt", "a", encoding="utf8") as file:
    for title in all_titles:
        file.write(f"{title}\n")

