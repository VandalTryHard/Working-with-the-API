import requests

headers = {'Authorization': 'token TOKEN',}

response = requests.get('https://api.github.com/rate_limit', headers=headers)

print(response)