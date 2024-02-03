from langchain_openai import ChatOpenAI

from api import API_key

llm = ChatOpenAI(
    openai_api_key=API_key(),
)

query = input()

print(f'[질문]: {query}')
print(f'[답변]: {llm.invoke(query)}')