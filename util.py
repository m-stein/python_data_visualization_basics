import requests


def request_json(url, headers):
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        print('Error: API request failed')
        exit(-1)

    return response.json()