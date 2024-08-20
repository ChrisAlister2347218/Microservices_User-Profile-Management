import requests

user_id = 1  # Change this to the ID of the user you want to delete
url = f'http://127.0.0.1:5000/users/{user_id}'

response = requests.delete(url)

print(response.status_code)
