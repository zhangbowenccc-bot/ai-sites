from tools.trend_finder import get_trends
from tools.content_generator import generate_article

import os

print("AI Business V10 SEO网站系统启动")

trends = get_trends()

if not os.path.exists("sites"):
    os.mkdir("sites")

max_sites = 5
articles_per_site = 6

for i, trend in enumerate(trends[:max_sites]):

    site_folder = f"sites/site_{i+1}"

    if not os.path.exists(site_folder):
        os.mkdir(site_folder)

    print(f"\n===== 创建SEO网站 {i+1}: {trend} =====")

    article_links = ""

    for j in range(articles_per_site):

        article = generate_article(trend)

        article_file = f"article_{j+1}.html"
        article_path = f"{site_folder}/{article_file}"

        html = f"""
<!DOCTYPE html>
<html>

<head>

<title>{trend} Guide {j+1}</title>

<meta name="description" content="{trend} tutorial and guide">

<style>

body {{
font-family: Arial;
background:#f4f4f4;
margin:0;
}}

header {{
background:#111;
color:white;
padding:30px;
text-align:center;
}}

nav {{
background:#333;
padding:10px;
text-align:center;
}}

nav a {{
color:white;
margin:10px;
text-decoration:none;
}}

.container {{
max-width:900px;
margin:auto;
background:white;
padding:30px;
margin-top:20px;
}}

footer {{
background:#111;
color:white;
text-align:center;
padding:20px;
margin-top:40px;
}}

</style>

</head>

<body>

<header>

<h1>{trend}</h1>

</header>

<nav>

Home
Tools
Guides

</nav>

<div class="container">

<h2>{trend} Guide</h2>

<p>{article}</p >

</div>

<footer>

<p>AI SEO Website V10</p >

</footer>

</body>

</html>
"""

        with open(article_path, "w", encoding="utf-8") as f:
            f.write(html)

        article_links += f'<li>Guide {j+1}</li>'

    # 分类页
    category_html = f"""
<html>

<head>

<title>{trend} Tools</title>

</head>

<body>

<h1>{trend} Tools</h1>

<ul>

{article_links}

</ul>

</body>

</html>
"""

    with open(f"{site_folder}/category_tools.html", "w", encoding="utf-8") as f:
        f.write(category_html)

    with open(f"{site_folder}/category_guides.html", "w", encoding="utf-8") as f:
        f.write(category_html)

    # 首页
    index_html = f"""
<html>

<head>

<title>{trend} Website</title>

</head>

<body>

<h1>{trend}</h1>

<h2>Latest Guides</h2>

<ul>

{article_links}

</ul>

</body>

</html>
"""

    with open(f"{site_folder}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

print("\nAI SEO 网站系统 V10 完成")