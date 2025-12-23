from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun


load_dotenv()

search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke('top news in bangladesh today')

print(result)

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

result = model.invoke('hi')

print('='* 100)
print(result.content)
print('='* 100)