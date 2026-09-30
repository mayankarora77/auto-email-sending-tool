from tavily_client import research_company

results = research_company("OpenAI")

for result in results:
    print("Title:", result.get("title"))
    print("URL:", result.get("url"))
    print("Content:", result.get("content"))
    print("-" * 50)