from executor import run_business
from tools.trend_finder import get_trends
from tools.content_generator import generate_article

import os

print("AI Business V6 网站工厂启动")

trends = get_trends()

# 创建主目录
if not os.path.exists("sites"):
    os.mkdir("sites")

if not os.path.exists("articles"):
    os.mkdir("articles")

for i, trend in enumerate(trends):

    site_folder = f"sites/site_{i+1}"

    if not os.path.exists(site_folder):
        os.mkdir(site_folder)

    print(f"\n===== 创建AI网站 {i+1}: {trend} =====")

    # 生成网站主页
    run_business(trend)

    if os.path.exists("output_site.html"):
        os.rename("output_site.html", f"{site_folder}/index.html")

    print("生成SEO文章...")

    for j in range(3):

        article = generate_article(trend)

        article_file = f"article_{j+1}.html"
        article_path = f"{site_folder}/{article_file}"

        html = f"""
        <html>
        <head>
        <title>{trend} - Article {j+1}</title>
        </head>

        <body>

        <h1>{trend}</h1>

        <p>{article}</p >

        返回首页

        </body>
        </html>
        """

        with open(article_path, "w", encoding="utf-8") as f:
            f.write(html)

print("\nAI网站工厂完成")