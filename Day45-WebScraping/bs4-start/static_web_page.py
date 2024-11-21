from bs4 import BeautifulSoup
import requests

with requests.get(url="https://appbrewery.github.io/news.ycombinator.com/") as response:
    content = response.text

soup = BeautifulSoup(content, "html.parser")

all_titles = soup.find_all(name="a", class_="storylink")
all_scores = soup.find_all(name="span", class_="score")

text = []
score = []
links = []
for i in range(len(all_titles)):
    text.append(all_titles[i].getText())
    links.append(all_titles[i].get("href"))
    score.append(int(all_scores[i].getText().split()[0]))


max_upvote = max(score)
its_index = score.index(max_upvote)
print(text[its_index])
print(links[its_index])
















# with open("./website.html") as html_file:
#     content = html_file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# all_anchors = soup.find(id="name")
#
# print(all_anchors.string)






