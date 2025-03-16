
from groq import Groq

client = Groq(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)