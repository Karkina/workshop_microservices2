import requests

url = 'https://deal-init-staging.herokuapp.com/api/v1/initDeals'

x = requests.get(url)
print(x)