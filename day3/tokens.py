import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Key Not Found.....!")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="What is Agentic AI?"

message1={
    "role":"system",
    "content":"You are my loving gf"
}

message={
    "role":role,
    "content":prompt
}

messages=[message1,message]

response=client.chat.completions.create(model=model,messages=messages,temperature=2,max_tokens=200)
print(response.choices[0].message.content)

usage=response.usage
print(f"Token cosumed by prompt are {usage.prompt_tokens} and tokens consumed by resposne are {usage.completion_tokens} Fininsh reason {response.choices[0].finish_reason} ")