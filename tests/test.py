import pytest
import requests


def test_swagger():

    model_endpoint = 'http://localhost:5000/swagger.json'

    r = requests.get(url=model_endpoint)
    assert r.status_code == 200
    assert r.headers['Content-Type'] == 'application/json'

    json = r.json()
    assert 'swagger' in json
    assert json.get('info') and json.get('info').get('title') == 'Model Asset Exchange Server'


def test_metadata():

    model_endpoint = 'http://localhost:5000/model/metadata'

    r = requests.get(url=model_endpoint)
    assert r.status_code == 200

    metadata = r.json()
    assert metadata['id'] == 'im2txt-tensorflow'
    assert metadata['name'] == 'im2txt TensorFlow Model'
    assert metadata['description'] == 'im2txt TensorFlow model trained on MSCOCO'
    assert metadata['license'] == 'APACHE V2'
    assert 1 == 0


def test_predict():
    model_endpoint = 'http://localhost:5000/model/predict'
    file_path = 'assets/surfing.jpg'
    caption_text = 'a man riding a wave on top of a surfboard .'

    with open(file_path, 'rb') as file:
        file_form = {'image': (file_path, file, 'image/jpeg')}
        r = requests.post(url=model_endpoint, files=file_form)

    assert r.status_code == 200
    response = r.json()
    assert response['status'] == 'ok'
    assert response['predictions'][0]['caption'] == caption_text


if __name__ == '__main__':
    pytest.main([__file__])
