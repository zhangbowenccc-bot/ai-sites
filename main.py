from agents.trend_agent import find_trends
from agents.research_agent import research
from agents.content_agent import write_article
from agents.product_agent import create_pdf

topic = input("输入赚钱领域: ")

print("\nAI寻找趋势...\n")

trends = find_trends(topic)

print(trends)

selected = input("\n选择一个方向: ")

print("\nAI研究资料...\n")

data = research(selected)

print(data)

print("\nAI生成内容...\n")

article = write_article(selected, data)

print(article)

print("\n生成产品...\n")

create_pdf(article)

print("\n完成，PDF已生成")