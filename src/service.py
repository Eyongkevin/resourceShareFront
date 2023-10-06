# from . import api_mock as api
from . import api


def login_user(username, password):
    try:
        res = api.login_user(username=username, password=password)
        return {
            "message": "success",
            "status_code": res.status_code,
            "token": res.json().get("token"),
        }
    except:
        return {"message": "failed", "error": "Something wrong happened"}
