from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")

def write_article(topic):

    prompt = f"""
写一篇1000字文章。

主题:
{topic}
"""

    return llm.invoke(prompt)