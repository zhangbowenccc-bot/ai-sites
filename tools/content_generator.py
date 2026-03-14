from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")

def generate_article(topic):

    prompt = f"""
你是SEO写作专家。

主题:
{topic}

写一篇SEO文章。

要求:
1000字
包含标题
包含小标题
适合网站流量
"""

    return llm.invoke(prompt)