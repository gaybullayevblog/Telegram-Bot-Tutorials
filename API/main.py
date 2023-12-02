import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/f04b5214af04b89d952e970f/pair/USD/UZS'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)