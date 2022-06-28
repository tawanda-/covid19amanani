from api import create_app

def test_index(client):
    response = client.get('/country/test')
    assert response.json['hello'] == 'world'