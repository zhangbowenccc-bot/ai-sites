import os
import re
from tools.trend_finder import get_trends
from tools.content_generator import generate_article
from langchain_ollama import OllamaLLM

print("AI SEO Factory V31 启动")

llm = OllamaLLM(model="qwen2:7b")

trends = get_trends()

if not os.path.exists("site"):
    os.mkdir("site")

def slugify(text):

    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = text.replace(" ","-")

    return text


def create_css():

    css = """
body{
font-family:Arial;
max-width:900px;
margin:auto;
padding:20px;
line-height:1.6;
}

h1{
color:#222;
}

a{
color:#0066cc;
}

nav{
margin-bottom:20px;
}

footer{
margin-top:40px;
color:#777;
}
"""

    with open("site/style.css","w") as f:
        f.write(css)


create_css()

home_links = ""

for i,trend in enumerate(trends[:5]):

    folder = f"site/site_{i+1}"

    if not os.path.exists(folder):
        os.mkdir(folder)

    print("创建网站:",trend)

    keywords = [

    f"{trend} guide",
    f"{trend} tutorial",
    f"{trend} tips",
    f"{trend} tools",
    f"{trend} examples"

    ]

    links = ""

    for keyword in keywords:

        title = keyword
        slug = slugify(title)

        filename = f"{slug}.html"

        print("生成文章:",title)

        content = generate_article(title)

        html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<link rel="stylesheet" href="../style.css">
</head>

<body>

<nav>
Home
</nav>

<h1>{title}</h1>

<p>{content}</p >

</body>
</html>
"""

        with open(f"{folder}/{filename}","w",encoding="utf-8") as f:
            f.write(html)

        links += f'<li>{title}</li>'


    index_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{trend}</title>
<link rel="stylesheet" href="../style.css">
</head>

<body>

<h1>{trend}</h1>

<ul>

{links}

</ul>

</body>
</html>
"""

    with open(f"{folder}/index.html","w",encoding="utf-8") as f:
        f.write(index_html)

    home_links += f'<li>{trend}</li>'


home_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>AI Generated Sites</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<h1>AI SEO Sites</h1>

<ul>

{home_links}

</ul>

</body>
</html>
"""

with open("site/index.html","w",encoding="utf-8") as f:
    f.write(home_html)

robots = """
User-agent: *
Allow: /
"""

with open("site/robots.txt","w") as f:
    f.write(robots)

print("AI SEO Factory V31 完成")