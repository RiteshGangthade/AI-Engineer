import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel


load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Key Not Found.....!")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

class Application(BaseModel):
    Name:str
    Experience: str
    Tech_stack: str
    Preferred_loc: list[str]

schema=Application.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt=f"""
You are a technical recruiter.

Extract the candidate information.

Return the response ONLY in JSON.

Use this schema:

{schema}
"""

system_message={
    "role": "system",
    "content": system_prompt
}

role="user"
text="Myself Lala,I am software developer with 2.6 years of exp in java and with 30days notice period and preferring location as Pune"
prompt=f"""
Here is one of msg from candidate I want personal infirmation from this {text}
"""

message={
    "role":role,
    "content":prompt
}

messages=[system_message,message]

response=client.chat.completions.create(model=model,messages=messages,temperature=2,response_format=response_format)
print(response.choices[0].message.content)

