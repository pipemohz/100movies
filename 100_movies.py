from bs4 import BeautifulSoup
import requests
import json

request = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

movies_html = request.content

html = BeautifulSoup(movies_html, "html.parser")
data = json.loads(html.select_one("#__NEXT_DATA__").contents[0])


# div = html.find(name="h3", class_="jsx-4245974604")
#div = html.select_one(".listicle-container.jsx-3523802742 .listicle-item.jsx-3523802742")
#div = html.select_one(selector=".listicle-container.jsx-3523802742")


# uncomment this to print all data:
#print(json.dumps(data))


def find_articles(data):
    if isinstance(data, dict):
        for k, v in data.items():
            if k.startswith("ImageMeta:"):
                yield v["titleText"]
            else:
                yield from find_articles(v)
    elif isinstance(data, list):
        for i in data:
            yield from find_articles(i)


for a in find_articles(data):
    print(a)