from ddgs import DDGS

def get_trends():

    trends = []

    topics = [
        "AI tools",
        "AI business",
        "AI automation",
        "AI marketing",
        "AI startup",
        "AI赚钱",
        "AI副业"
    ]

    with DDGS() as ddgs:

        for topic in topics:

            results = ddgs.text(topic, max_results=5)

            for r in results:

                if "title" in r:
                    trends.append(r["title"])

    return trends[:10]