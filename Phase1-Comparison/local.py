import ollama
import time

start = time.perf_counter()

result = ollama.chat(
    model = "qwen3:8b",
    messages=[
        {
            "role" : "system",
            "content" : "You are an expert AI engineer"
        },
        {
            "role" : "user",
            "content" : "explain What is a neural network"
        }
        
    ],
    stream=False
)

end = time.perf_counter()

tokens = result.prompt_eval_count + result.eval_count;

print (f" Local model: {result.message.content} \n ")
print(f"Latency = {end-start} seconds")
print(f"Tokens used= {tokens}")


