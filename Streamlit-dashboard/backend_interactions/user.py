import requests

def get_user(token):
    url_post = "http://127.0.0.1:8004/users/me/"
    user = requests.get(url_post, headers={'Authorization':f'Bearer {token}'})
    print(user)
    print(user.json())
    return user.json()

def get_token(username, password):


    url = "http://127.0.0.1:8004/token"

    payload= f'grant_type=&username={username}&password={password}&scope=&client_id=&client_secret='
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'accept': 'application/json'
    }

    token = requests.post(url, headers=headers, data=payload)

    print(token.text)
    return token.json()["access_token"]
