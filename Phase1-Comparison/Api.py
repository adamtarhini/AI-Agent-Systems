import ollama
import os 
from ollama import Client,chat
import time
from dotenv import load_dotenv

load_dotenv()

start = time.perf_counter()

client = Client(
    host="https://ollama.com/" ,
    headers={'Authorization': 'Bearer ' + os.environ.get('Api_Key')}
)

result = client.chat(
    model = 'gemma4',
    messages = [
        {
                    "role" : "system",
                    "content" : "You are an expert AI engineer"
                },
                {
                    "role" : "user",
                    "content" : "explain What is a neural network"
                }
                
    ]
)

end = time.perf_counter()
tokens = result.eval_count + result.prompt_eval_count

token_input_price = 0.07/1000000
token_output_price = 0.34/1000000

total_cost = token_input_price*result.prompt_eval_count + token_output_price*result.eval_count

print(f"ollama cloud: {result.message.content}")
print(f"Latency = {end-start} seconds")
print(f"Tokens used= {tokens}")
print(f"cost= {total_cost}")


