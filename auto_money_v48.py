import os
import datetime
import random
import subprocess
from langchain_ollama import OllamaLLM
from tools.trend_finder import get_trends

# -------------------------------
# 配置
# -------------------------------
BASE_DIR = "site"
MAX_SITES = 10            # 子站数量，可按需扩展
ARTICLES_PER_SITE = 25     # 每个子站文章数量
LANGUAGES = ["en", "zh"]
GITHUB_REPO_DIR = "D:/AI-Agent/AI-Business"
BRANCH = "main"

llm = OllamaLLM(model="qwen2:7b")

# -------------------------------
# 工具函数
# -------------------------------
def slugify(text):
    return text.lower().replace(" ", "-")

def generate_keywords(topic):
    prompt = f"你是SEO专家，为主题 '{topic}' 生成30个SEO关键词，每行一个关键词"
    result = llm.invoke(prompt)
    return [k.strip() for k in result.split("\n") if k.strip()]

def generate_article(title, lang="en"):
    prompt = f"""
写一篇原创SEO文章
标题: {title}
语言: {lang}
要求:
- 3000到5000字
- 分段清晰
- 多个小标题
- 内部推荐文章5-8条
- 初学者友好
"""
    return llm.invoke(prompt)

def create_article_html(title, content, lang="en", related_links=None):
    link_html = ""
    if related_links:
        link_html = "<h3>Related Articles</h3><ul>"
        for l in related_links:
            link_html += f'<li><a href="{l}">{l.replace("_en","")}</a></li>'
        link_html += "</ul>"

    ad_block = "<div style='margin:20px 0; padding:10px; border:1px dashed #ccc; text-align:center;'>Ad Placeholder</div>"

    html = f"""
<html>
<head>
<meta charset="UTF-8">
<title>{title} ({lang})</title>
<link rel="stylesheet" href="style.css">
<meta name="description" content="{title} guide">
<meta name="keywords" content="{title}, AI, SEO, tools">
</head>
<body>
<h1>{title} ({lang})</h1>
{content}
{link_html}
{ad_block}
<nav>
<a href="index.html">Back to Site Home</a>
<a href="../index.html">Back to Main Home</a>
</nav>
</body>
</html>
"""
    return html

def create_site(site_id, trend):
    site_path = f"{BASE_DIR}/site_{site_id}"
    os.makedirs(site_path, exist_ok=True)

    keywords = generate_keywords(trend)
    article_files = []

    for i, keyword in enumerate(keywords[:ARTICLES_PER_SITE]):
        for lang in LANGUAGES:
            title = keyword
            slug = slugify(title) + f"_{lang}"
            filename = f"{slug}.html"
            print(f"[Site {site_id}] Generating: {title} ({lang})")
            related_links = random.sample(article_files, min(8, len(article_files))) if article_files else None
            article = generate_article(title, lang)
            html = create_article_html(title, article, lang, related_links)
            with open(f"{site_path}/{filename}", "w", encoding="utf-8") as f:
                f.write(html)
            if lang=="en":
                article_files.append(filename)

    # 子站首页
    index_html = "<html><head><meta charset='UTF-8'><title>{}</title><link rel='stylesheet' href='style.css'></head><body>".format(trend)
    index_html += f"<h1>{trend}</h1><ul>"
    for f in article_files:
        index_html += f'<li><a href="{f}">{f.replace("_en.html","")}</a></li>'
    index_html += "</ul><a href='../index.html'>Back to Main Home</a></body></html>"

    with open(f"{site_path}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

def create_home(trends):
    html = "<html><head><meta charset='UTF-8'><title>AI SEO Network</title><link rel='stylesheet' href='style.css'></head><body>"
    html += "<header><h1>AI SEO Network</h1></header><nav><ul>"
    for i, trend in enumerate(trends[:MAX_SITES], start=1):
        html += f'<li><a href="site_{i}/index.html">{trend}</a></li>\n'
    html += "</ul></nav></body></html>"
    with open(f"{BASE_DIR}/index.html", "w", encoding="utf-8") as f:
        f.write(html)

def create_style():
    css = """
body { font-family: Arial; max-width: 1000px; margin:auto; padding:20px; line-height:1.6; }
header { background:#f8f8f8; padding:10px; text-align:center; }
nav ul { list-style-type:none; padding:0; display:flex; gap:10px; flex-wrap:wrap; }
nav ul li { display:inline; }
a { color:#0066cc; text-decoration:none; }
a:hover { text-decoration:underline; }
h1 { color:#222; }
"""
    with open(f"{BASE_DIR}/style.css","w", encoding="utf-8") as f:
        f.write(css)

def create_sitemap():
    sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    for i in range(1, MAX_SITES+1):
        sitemap += f"<url><loc>/site_{i}/</loc></url>\n"
        for a in range(1, ARTICLES_PER_SITE+1):
            sitemap += f"<url><loc>/site_{i}/article_{a}_en.html</loc></url>\n"
            sitemap += f"<url><loc>/site_{i}/article_{a}_zh.html</loc></url>\n"
    sitemap += "</urlset>"
    with open(f"{BASE_DIR}/sitemap.xml","w", encoding="utf-8") as f:
        f.write(sitemap)

def github_push():
    os.chdir(GITHUB_REPO_DIR)
    subprocess.run(["git","add","."],check=True)
    subprocess.run(["git","commit","-m",f"V48 update {datetime.datetime.now()}"],check=True)
    subprocess.run(["git","push","origin",BRANCH],check=True)
    print("GitHub push completed.")

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    create_style()
    trends = get_trends()[:MAX_SITES]

    for i, trend in enumerate(trends, start=1):
        create_site(i, trend)

    create_home(trends)
    create_sitemap()
    github_push()
    print("V48 AI SEO Fully Automated Money-Ready Mega Portal Completed")

if __name__ == "__main__":
    main()