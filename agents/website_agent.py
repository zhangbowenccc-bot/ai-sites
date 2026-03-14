from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2:7b")

def build_website(product, marketing):

    prompt = f"""
你是专业网站开发者。

根据产品和营销方案生成一个简单网站。

产品:
{product}

营销方案:
{marketing}

生成完整HTML页面。

要求：
1 有标题
2 产品介绍
3 优势
4 购买按钮
5 简单CSS
"""

    return llm.invoke(prompt)