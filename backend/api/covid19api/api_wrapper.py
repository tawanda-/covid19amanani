import requests
from enum import Enum

class Endpoints(Enum):
    LATEST = 'https://covid-api.mmediagroup.fr/v1/cases'
    VACCINES = 'https://covid-api.mmediagroup.fr/v1/vaccines'
    HISTORY = 'https://covid-api.mmediagroup.fr/v1/history'

def get(endpoint, parameters):

    response = None

    match endpoint:
        case 'latest':
            response = requests.get(Endpoints.LATEST, params=parameters)
        case 'vaccine':
            response = requests.get(Endpoints.VACCINES, params=parameters)
        case 'history':
            response = requests.get(Endpoints.HISTORY, params=parameters)
        case _:
            return None

    if response and response.status_code == 200:
        content = response.content
        return content
    else:
        return None