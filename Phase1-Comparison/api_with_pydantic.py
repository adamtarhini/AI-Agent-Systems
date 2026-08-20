import ollama
import os 
from ollama import Client,chat
import time
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import List

load_dotenv()

class Format(BaseModel):
    definition: str 
    layers: List[str]
    how_it_learns:str
    example : str
    

start = time.perf_counter()

client = Client(
    host="https://ollama.com/" ,
    headers={'Authorization': 'Bearer ' + os.environ.get('Api_Key')}
)



result = client.chat(
    model = 'gpt-oss:20b-cloud',
    messages = [
        {
                    "role" : "system",
                    "content" : "you are an ai expert and a Json generator"
                                f"Match this exact schema:\n{Format.model_json_schema()}\n\n"
                },
                {
                    "role" : "user",
                    "content" : "explain What is a neural network"
                }
    ],
    format=Format.model_json_schema(),
)



raw = result.message.content


final = Format.model_validate_json(raw)
print(final)
    
end = time.perf_counter()
tokens = result.eval_count + result.prompt_eval_count

token_input_price = 0.07/1000000
token_output_price = 0.34/1000000

total_cost = token_input_price*result.prompt_eval_count + token_output_price*result.eval_count

print(f"Latency = {end-start} seconds")
print(f"Tokens used= {tokens}")
print(f"cost= {total_cost}")


