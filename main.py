import requests
from base64 import b64encode

url = "https://free.gpt4free.lol/v1/"

payload = {
    "prompt": "What is the meaning of life?",
    "model": "adonai12free",  # Models = ["gpt5free", "adonai12free"], there still much more models but the other ones are paid
}

headers = {
    "Host": "free.gpt4free.lol",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    "x-vardxg": b64encode(
        "vardxg_is_g".encode()
    ).decode(),  # This is the required header for authentication
    "Content-Type": "application/json",
}

response = requests.post(url, headers=headers, json=payload)

print(response.text)
