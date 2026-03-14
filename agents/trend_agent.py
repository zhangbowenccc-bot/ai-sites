from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")

def find_trends(topic):

    prompt = f"""
你是互联网趋势专家。

领域:
{topic}

列出10个热门赚钱方向。
"""

    return llm.invoke(prompt)