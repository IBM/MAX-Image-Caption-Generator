import pytest
import requests


def test_response():
    model_endpoint = 'http://localhost:8088/model/predict'
    file_path = 'assets/surfing.jpg'
    caption_text = 'a man riding a wave on top of a surfboard .'

    with open(file_path, 'rb') as file:
        file_form = {'file': (file_path, file, 'image/jpeg')}
        r = requests.post(url=model_endpoint, files=file_form)

    assert r.status_code == 200
    response = r.json()
    assert response['status'] == 'ok'
    assert response['predictions'][0]['caption'] == caption_text


if __name__ == '__main__':
    pytest.main([__file__])
