import requests
from enum import Enum
from flask import current_app, json

class Endpoints(Enum):
    LATEST = 'https://covid-api.mmediagroup.fr/v1/cases'
    VACCINES = 'https://covid-api.mmediagroup.fr/v1/vaccines'
    HISTORY = 'https://covid-api.mmediagroup.fr/v1/history'

def get(endpoint, parameters):

    response = None

    match endpoint:
        case 'latest':
            response = requests.get(Endpoints.LATEST.value, params=parameters)
        case 'vaccine':
            response = requests.get(Endpoints.VACCINES.value, params=parameters)
        case 'history':
            return None
        case _:
            return None

    if response:
        content = response.json()
        return content
    else:
        return None   