'''
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3",
  "prompt":"hola",
  "stream": false
}'
'''
import requests

uri = "http://localhost:11434/api/generate"
data = {
  "model": "gemma3:1b",
  "prompt":"hola",
  "stream": False
}

response = requests.post(uri, json=data)

print(response)