from tools.baidu_trends import get_baidu_trends
from tools.cn_titles import generate_cn_titles
from tools.local_llm import generate_text

import os
import subprocess
import shutil

print("V51-CN+ AI内容工厂启动")

BASE_DIR="websites"

if os.path.exists(BASE_DIR):
    shutil.rmtree(BASE_DIR)

os.mkdir(BASE_DIR)

trends=get_baidu_trends("AI工具")

def generate_article(title):

    prompt=f"""
写一篇1000字中文SEO文章

标题:
{title}

要求
介绍AI工具
"""

    content=generate_text(prompt)

    html=f"""
<html>

<head>

<meta charset="utf-8">

<title>{title}</title>

<meta name="description" content="{title}">

</head>

<body>

<h1>{title}</h1>

<p>{content}</p >

</body>

</html>
"""

    return html


site_id=1

for trend in trends:

    titles=generate_cn_titles(trend)

    site_folder=f"{BASE_DIR}/site_{site_id}"

    os.mkdir(site_folder)

    links=""

    for title in titles:

        filename=title.replace(" ","")+".html"

        article=generate_article(title)

        with open(f"{site_folder}/{filename}","w",encoding="utf-8") as f:
            f.write(article)

        links+=f'<li>{title}</li>'

    index_html=f"""
<html>

<head>

<meta charset="utf-8">

<title>{trend}</title>

</head>

<body>

<h1>{trend}</h1>

<ul>

{links}

</ul>

</body>

</html>
"""

    with open(f"{site_folder}/index.html","w",encoding="utf-8") as f:
        f.write(index_html)

    site_id+=1


print("文章生成完成")

subprocess.run(["git","add","."])
subprocess.run(["git","commit","-m","AI auto update"])
subprocess.run(["git","push"])

print("GitHub更新完成")