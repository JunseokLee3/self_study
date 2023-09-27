import requests

target = 'https://jsonplaceholder.typicode.com/users/1'
response = requests.get(url=target)
print(response.text)