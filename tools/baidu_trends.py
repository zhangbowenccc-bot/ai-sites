import requests
from bs4 import BeautifulSoup


def get_baidu_trends(keyword="AI工具"):

    url = f"https://www.baidu.com/s?wd={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=10)

    soup = BeautifulSoup(r.text, "html.parser")

    trends = []

    for h in soup.select("h3")[:10]:

        text = h.get_text().strip()

        if text:
            trends.append(text)

    return trends