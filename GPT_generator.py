import openai
from utils import read_config

openai.api_key = read_config()["openai_api_key"]

def generate_GPT(message):
    
    reseponse = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        temperature=0.9,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.5,
    )

    return reseponse["choices"][0]["text"]