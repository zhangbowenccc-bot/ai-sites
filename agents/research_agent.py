from langchain_ollama import OllamaLLM
from tools.web_search import search_web

llm = OllamaLLM(model="qwen2:7b")

def research(topic):

    web = search_web(topic)

    prompt = f"""
根据以下资料整理知识。

{web}

主题:
{topic}
"""

    return llm.invoke(prompt)