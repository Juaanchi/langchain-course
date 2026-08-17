from unittest import result
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()
#llm = ChatOpenAI(model="gpt-4o")

#prompt = ChatPromptTemplate.from_template("What is the capital of {country}?")

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: search query
    Returns:
        str: search results
    """
    print(f"Searching for {query} ")
    #return "tokyo weather is sunny"
    return tavily.search(query=query)
    
llm = ChatOpenAI(model="gpt-4o-mini")
tools = [search]
agent = create_agent(model=llm, tools=tools)
    #result = agent.run("What is the weather in Tokyo?")
    #print(result)

def main():
        print("Hello from langchain-course!")
        result = agent.invoke({"messages":HumanMessage(content="busca 3 trabajos que busquen un Ingeniero IA / Automation Engineer en LinkedIn que solicite habilidades como N8N o Make. Y listame detalles de cada uno. Busco en España pero de forma remota.") })
        print(result)

if __name__ == "__main__":
    main()
