import os
import random

BASE_DIR = "site"

SITE_COUNT = 30
ARTICLES_PER_SITE = 30

keywords = [
    "AI tools",
    "AI automation",
    "AI productivity",
    "AI marketing",
    "AI coding tools",
    "AI design tools",
    "AI SEO tools",
    "AI writing tools",
    "AI business automation",
    "AI chatbot tools",
    "AI video generator",
    "AI image generator",
    "AI startup ideas",
    "AI workflow automation"
]


def generate_content(title):

    paragraphs = [

        f"{title} is becoming an important topic in the world of artificial intelligence.",

        "AI technology is transforming the way companies operate and build products.",

        "Modern startups rely heavily on automation tools to increase productivity.",

        "Businesses that adopt AI tools early often gain competitive advantages.",

        "Many professionals now integrate AI solutions into daily workflows.",

        "Learning how to use AI tools effectively can improve efficiency and innovation.",

        "As AI continues to evolve, new tools and platforms appear every year."

    ]

    body = ""

    for p in paragraphs:
        body += f"<p>{p}</p>\n"

    return body


def generate_article(title):

    content = generate_content(title)

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<meta name="description" content="{title} complete guide">
</head>

<body>

<h1>{title}</h1>

{content}

<a href="../index.html">Back</a>

</body>
</html>
"""

    return html


def create_site(site_id):

    site_path = f"{BASE_DIR}/site_{site_id}"
    os.makedirs(site_path, exist_ok=True)

    index_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AI Site {site_id}</title>
</head>

<body>

<h1>AI Site {site_id}</h1>

<ul>
"""

    for a in range(1, ARTICLES_PER_SITE + 1):

        kw = random.choice(keywords)

        title = f"{kw} Guide {a}"

        filename = f"article_{a}.html"

        index_html += f'<li><a href="{filename}">{title}</a></li>\n'

        article_html = generate_article(title)

        with open(f"{site_path}/{filename}", "w", encoding="utf-8") as f:
            f.write(article_html)

    index_html += """
</ul>

<a href="../index.html">Back to Home</a>

</body>
</html>
"""

    with open(f"{site_path}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)


def create_home():

    html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AI SEO Sites</title>
</head>

<body>

<h1>AI SEO Sites</h1>

<ul>
"""

    for i in range(1, SITE_COUNT + 1):

        html += f'<li><a href="site_{i}/index.html">AI Site {i}</a></li>\n'

    html += """
</ul>

</body>
</html>
"""

    with open(f"{BASE_DIR}/index.html", "w", encoding="utf-8") as f:
        f.write(html)


def create_sitemap():

    sitemap = ""

    for i in range(1, SITE_COUNT + 1):

        sitemap += f"/site_{i}/\n"

        for a in range(1, ARTICLES_PER_SITE + 1):

            sitemap += f"/site_{i}/article_{a}.html\n"

    with open(f"{BASE_DIR}/sitemap.txt", "w") as f:
        f.write(sitemap)


def main():

    os.makedirs(BASE_DIR, exist_ok=True)

    for i in range(1, SITE_COUNT + 1):

        print("Creating site", i)

        create_site(i)

    create_home()

    create_sitemap()

    print("V35 AI SEO network generated!")


if __name__ == "__main__":
    main()