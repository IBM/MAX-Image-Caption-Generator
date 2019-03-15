import pytest
import requests


def test_swagger():

    model_endpoint = 'http://localhost:5000/swagger.json'

    r = requests.get(url=model_endpoint)
    assert r.status_code == 200
    assert r.headers['Content-Type'] == 'application/json'

    json = r.json()
    assert 'swagger' in json
    assert json.get('info') and json.get('info').get('title') == 'MAX Image Caption Generator'


def test_metadata():

    model_endpoint = 'http://localhost:5000/model/metadata'

    r = requests.get(url=model_endpoint)
    assert r.status_code == 200

    metadata = r.json()
    assert metadata['id'] == 'max-image-caption-generator'
    assert metadata['name'] == 'MAX Image Caption Generator'
    assert metadata['description'] == 'im2txt TensorFlow model trained on MSCOCO'
    assert metadata['license'] == 'Apache 2.0'
    assert metadata['type'] == 'Image-to-Text Translation'
    assert 'max-image-caption-generator' in metadata['source']


def _check_response(r):
    caption_text = 'a man riding a wave on top of a surfboard .'
    assert r.status_code == 200
    response = r.json()
    assert response['status'] == 'ok'
    assert response['predictions'][0]['caption'] == caption_text


def test_predict():
    model_endpoint = 'http://localhost:5000/model/predict'
    formats = ['jpg', 'png']
    file_path = 'tests/surfing.{}'
    
    for f in formats:
        p = file_path.format(f)
        with open(p, 'rb') as file:
            file_form = {'image': (p, file, 'image/{}'.format(f))}
            r = requests.post(url=model_endpoint, files=file_form)
        _check_response(r)


if __name__ == '__main__':
    pytest.main([__file__])
