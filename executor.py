from agents.ceo_agent import ceo_decide
from agents.trend_agent import find_trends
from agents.analyst_agent import analyze_market
from agents.product_agent import design_product
from agents.marketing_agent import create_marketing
from agents.website_agent import build_website


def run_business(topic):

    print("\nCEO制定战略...\n")
    strategy = ceo_decide(topic)
    print(strategy)

    print("\n研究趋势...\n")
    trends = find_trends(topic)
    print(trends)

    print("\n市场分析...\n")
    analysis = analyze_market(topic)
    print(analysis)

    print("\n产品设计...\n")
    product = design_product(topic)
    print(product)

    print("\n营销策略...\n")
    marketing = create_marketing(topic)
    print(marketing)

    print("\n生成网站...\n")
    website = build_website(product, marketing)

    with open("output_site.html", "w", encoding="utf-8") as f:
        f.write(website)

    print("\n网站已生成: output_site.html")