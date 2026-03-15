import os

BASE_DIR = "site"
SITE_COUNT = 5
ARTICLES_PER_SITE = 5


def create_index():
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


def create_article(site_id, article_id):

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AI Tool Guide {article_id}</title>
</head>

<body>

<h1>AI Tool Guide {article_id}</h1>

<p>This article explains useful AI tools for productivity.</p>

<p>Artificial intelligence is transforming industries and workflows.</p>

<p>More guides coming soon.</p>

<a href="../index.html">Back</a>

</body>
</html>
"""

    return html


def create_sites():

    os.makedirs(BASE_DIR, exist_ok=True)

    for i in range(1, SITE_COUNT + 1):

        site_path = f"{BASE_DIR}/site_{i}"
        os.makedirs(site_path, exist_ok=True)

        index_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AI Site {i}</title>
</head>

<body>

<h1>AI Site {i}</h1>

<ul>
"""

        for a in range(1, ARTICLES_PER_SITE + 1):

            article_name = f"article_{a}.html"

            index_html += f'<li><a href="{article_name}">Article {a}</a></li>\n'

            article_html = create_article(i, a)

            with open(f"{site_path}/{article_name}", "w", encoding="utf-8") as f:
                f.write(article_html)

        index_html += """
</ul>

<a href="../index.html">Back to Home</a>

</body>
</html>
"""

        with open(f"{site_path}/index.html", "w", encoding="utf-8") as f:
            f.write(index_html)


def main():

    create_sites()
    create_index()

    print("V33 AI SEO factory generated!")


if __name__ == "__main__":
    main()