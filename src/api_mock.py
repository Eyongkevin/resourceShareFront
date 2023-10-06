import requests

BASE_URL = "https://ff2fcdbf-b225-4d11-b92d-f64aaf15e0b4.mock.pstmn.io/"
login_url = BASE_URL + "v1/user/login/"


def login_user(*, username, password):
    response = requests.post(
        login_url, json={"username": username, "password": password}
    )
    if response:
        return response
    response.raise_for_status()
