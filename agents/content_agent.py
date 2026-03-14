from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")

def write_article(topic, research):

    prompt = f"""
写一篇2000字文章。

主题:
{topic}

资料:
{research}
"""

    return llm.invoke(prompt)