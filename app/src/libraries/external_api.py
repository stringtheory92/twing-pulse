import requests


def fetch_data_from_api(endpoint, params):
    response = requests.get(endpoint, params=params)
    return response.json()
