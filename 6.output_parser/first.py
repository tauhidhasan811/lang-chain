from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Writea detailed report on {topic}" ,
    input_variables=['topic']
    )

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text} ",
    input_variables=['text']
    )

promt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(promt1)

prompt2 = template2.invoke({'text': result.content})