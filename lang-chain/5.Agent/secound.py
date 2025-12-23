from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentState
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
prompt = "hi"

response = model.invoke(prompt)
print(response.content)

