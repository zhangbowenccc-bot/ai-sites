import os
import random

BASE_DIR = "site"
SITE_COUNT = 5
ARTICLES_PER_SITE = 10

topics = [
    "AI tools",
    "AI automation",
    "ChatGPT guide",
    "best AI tools 2026",
    "AI business ideas"
]

os.makedirs(BASE_DIR, exist_ok=True)

def create_article(title, path):

    content = f"""
<html>
<head>
<title>{title}</title>
</head>

<body>

<h1>{title}</h1>

<p>This article explains {title}.</p >

<p>AI is transforming the world and new tools appear every day.</p >

<p>Learning AI tools can help you build automation and online business.</p >

</body>
</html>
"""

    with open(path, "w", encoding="utf8") as f:
        f.write(content)


def create_site(site_id):

    site_folder = f"{BASE_DIR}/site_{site_id}"
    os.makedirs(site_folder, exist_ok=True)

    links = ""

    for i in range(ARTICLES_PER_SITE):

        title = random.choice(topics) + f" {i+1}"
        filename = f"article_{i+1}.html"

        create_article(title, f"{site_folder}/{filename}")

        links += f'<li>{title}</li>\n'

    index_html = f"""
<html>
<head>
<title>Site {site_id}</title>
</head>

<body>

<h1>Articles</h1>

<ul>

{links}

</ul>

</body>
</html>
"""

    with open(f"{site_folder}/index.html","w",encoding="utf8") as f:
        f.write(index_html)


def create_main_index():

    links = ""

    for i in range(1, SITE_COUNT+1):

        links += f'<li>AI Site {i}</li>\n'

    html = f"""
<html>
<head>
<title>AI SEO Sites</title>
</head>

<body>

<h1>AI SEO Sites</h1>

<ul>

{links}

</ul>

</body>
</html>
"""

    with open(f"{BASE_DIR}/index.html","w",encoding="utf8") as f:
        f.write(html)


print("Generating sites...")

for i in range(1, SITE_COUNT+1):
    create_site(i)

create_main_index()

print("Done!")