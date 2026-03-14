from tools.trend_finder import get_trends
from tools.content_generator import generate_article
from langchain_ollama import OllamaLLM

import os
import re

print("AI Trend SEO System V24 启动")

llm = OllamaLLM(model="qwen2:7b")

trends = get_trends()

# 创建网站目录
if not os.path.exists("websites"):
    os.mkdir("websites")

max_sites = 5


# 安全URL函数
def slugify(text):

    text = text.lower()

    text = re.sub(r"[^\w\s-]", "", text)

    text = text.replace(" ", "-")

    return text


# 生成SEO关键词
def generate_keywords(topic):

    prompt = f"""
你是SEO专家。

为以下主题生成20个SEO关键词。

主题:
{topic}

每行一个关键词
"""

    result = llm.invoke(prompt)

    keywords = result.split("\n")

    keywords = [k.strip() for k in keywords if k.strip() != ""]

    return keywords


# 主循环
for i, trend in enumerate(trends[:max_sites]):

    site_folder = f"websites/site_{i+1}"

    if not os.path.exists(site_folder):
        os.mkdir(site_folder)

    print("\n创建趋势网站:", trend)

    keywords = generate_keywords(trend)

    post_links = ""

    for keyword in keywords[:10]:

        title = keyword

        slug = slugify(title)

        filename = f"{slug}.html"

        print("生成文章:", title)

        content = generate_article(title)

        html = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="utf-8">

<title>{title}</title>

<meta name="description" content="{title} complete guide">

<meta name="viewport" content="width=device-width, initial-scale=1">

</head>

<body>

<h1>{title}</h1>

<p>{content}</p >

</body>

</html>
"""

        with open(f"{site_folder}/{filename}", "w", encoding="utf-8") as f:
            f.write(html)

        post_links += f'<li>{title}</li>'

    index_html = f"""
<!DOCTYPE html>
<html>

<head>

<meta charset="utf-8">

<title>{trend} Blog</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

</head>

<body>

<h1>{trend}</h1>

<ul>

{post_links}

</ul>

</body>

</html>
"""

    with open(f"{site_folder}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

print("\nAI Trend SEO System V24 完成")