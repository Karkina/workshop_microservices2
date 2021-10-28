import requests

url = 'http://127.0.0.1:8000/snippets/3'

x = requests.delete(url)

print(x)