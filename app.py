import groq
import os                                                                                                                                                                                                          
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("API_KEY"))

client = groq.Groq(api_key=os.getenv("API_KEY"))

response = client.chat.completions.create(messages=[
    {
        "role": "assistant",
        "content": '''''',
    }
],
model="llama3-70b-8192",
)

generated_text = response.choices[0].message.content
print(generated_text)