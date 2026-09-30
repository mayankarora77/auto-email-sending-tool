import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=TAVILY_API_KEY)


def research_company(company: str):
    response = client.search(
        query=f"{company} official website products services recent news",
        search_depth="advanced",
        max_results=5
    )

    return response["results"]