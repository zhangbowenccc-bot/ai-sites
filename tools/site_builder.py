def save_site(html):

    with open("output_site.html","w",encoding="utf-8") as f:

        f.write(html)

    print("网站已生成: output_site.html")