from bs4 import BeautifulSoup
import requests

with requests.get(url="https://news.ycombinator.com/news") as response:
    content = response.text

soup = BeautifulSoup(content, "html.parser")

all_titles = soup.find_all(name="span", class_="titleline")
all_upvote = soup.find_all(name="span", class_="score")

titles = []
links = []
upvotes = []
for title in all_titles:
    titles.append(title.getText())
    links.append(title.find(name="a").get("href"))
for upvote in all_upvote:
    upvotes.append(int(upvote.getText().split()[0]))

# Above code would give incorrect results if all articles don't have upvotes yet
# Below code solves the problem
# subtexts = soup.findAll(class_="subtext")
# upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

max_upvote = max(upvotes)
its_index = upvotes.index(max_upvote)
print(titles[its_index])
print(links[its_index])



