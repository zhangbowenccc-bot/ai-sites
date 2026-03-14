from executor import run_business
from tools.trend_finder import get_trends
from tools.content_generator import generate_article

import os
import shutil

print("AI赚钱工厂启动")

trends = get_trends()

# 创建目录
if not os.path.exists("sites"):
    os.mkdir("sites")

if not os.path.exists("articles"):
    os.mkdir("articles")

for i, trend in enumerate(trends):

    print(f"\n===== AI创业项目 {i+1}: {trend} =====")

    # 生成网站
    run_business(trend)

    # 目标路径
    target = f"sites/site_{i+1}.html"

    # 如果文件已存在就删除
    if os.path.exists(target):
        os.remove(target)

    # 移动网站文件
    shutil.move("output_site.html", target)

    print("生成SEO文章...")

    # 生成文章
    article = generate_article(trend)

    # 保存文章
    article_path = f"articles/article_{i+1}.txt"
    with open(article_path, "w", encoding="utf-8") as f:
        f.write(article)

print("\nAI赚钱系统完成")