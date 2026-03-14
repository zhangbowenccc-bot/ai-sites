from langchain_ollama import OllamaLLM
from tools.web_search import search_web

llm = OllamaLLM(model="qwen2:7b")

def analyze_market(topic):

    web = search_web(topic)

    prompt = f"""
你是商业分析专家。

主题:
{topic}

互联网信息:
{web}

分析：

1 市场需求
2 竞争情况
3 盈利机会
"""

    return llm.invoke(prompt)