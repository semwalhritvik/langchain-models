from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# from huggingface_hub import login # Old format, now deprecated 
# login()

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", # model
    task="text-generation"
)

model = ChatHuggingFace(llm = llm )

result = model.invoke("What is the capital of Malaysia?")
print(result)
