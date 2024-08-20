import requests

user_id = 1  # Change this to the ID of the user you want to update
url = f'http://127.0.0.1:5000/users/{user_id}'
data = {
    'username': 'johnsmith',
    'email': 'johnsmith@example.com',
    'password': 'newsecurepassword'
}

response = requests.put(url, json=data)

print(response.status_code)
print(response.json())
