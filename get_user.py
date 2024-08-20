import requests

user_id = 1  # Change this to the ID of the user you want to retrieve
url = f'http://127.0.0.1:5000/users/{user_id}'

response = requests.get(url)

print(response.status_code)
print(response.json())
