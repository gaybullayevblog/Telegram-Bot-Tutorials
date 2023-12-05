import requests
from pprint import pprint as print

API_KEY = 'f04b5214af04b89d952e970f'

currency = 'USD'
url = 'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS'

response = requests.get(url)
print(response.status_code)
print(response.json())