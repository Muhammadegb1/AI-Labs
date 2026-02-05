import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

system_prompt = """You are an expert communications assistant. 
Your task is to analyze the body of an email and suggest a concise, professional, 
and highly relevant subject line (maximum 7 words). 
Focus on the 'Call to Action' or the primary purpose of the message."""

user_prompt = """
Hi Team,

I hope you're all having a productive week. I've finished reviewing 
the quarterly financial reports and noticed a few discrepancies in 
the marketing spend for November. 

Can we jump on a quick 15-minute call tomorrow at 10:00 AM to 
reconcile these numbers before we present to the board? 

Best,
Sarah
"""
def generate_subject(email_body):
    messages = [        
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": email_body }
    ]

    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    return response.choices[0].message.content

subject = generate_subject(user_prompt)
print("Suggested Subject:", subject)