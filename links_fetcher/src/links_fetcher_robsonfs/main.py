import requests

def get_source(url: str) -> (int, str):
    try:
        resp = requests.get(url)
    except Exception as err:
        raise Exception("Could not fetch the provided URL")

    return resp.status_code, resp.text
