import requests

BASE_URL = "http://127.0.0.1:8000/"
login_url = BASE_URL + "user/api/v1/login/"


def login_user(*, username, password):
    response = requests.post(
        login_url, json={"username": username, "password": password}
    )
    if response:
        return response
    response.raise_for_status()
