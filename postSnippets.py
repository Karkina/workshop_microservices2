import requests

url = 'http://127.0.0.1:8000/snippets/'
myobj = {"id": 5, "title": "", "code": "print(\"Anoujean\")\n", "linenos": False, "language": "python", "style": "friendly"}

x = requests.post(url, data = myobj)

