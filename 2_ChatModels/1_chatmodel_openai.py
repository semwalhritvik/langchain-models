from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
#All LLMs inherit BaseLLM class while all chat models inherit BaseChatModel class

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", temperature= 0.3, max_completion_tokens=10) 

result = model.invoke("What is the capital of Massachusetts?")
print(result.content)
