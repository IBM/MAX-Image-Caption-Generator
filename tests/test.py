import pytest
import pycurl
import io
import json


def test_response():
    c = pycurl.Curl()
    b = io.BytesIO()
    c.setopt(pycurl.URL, 'http://localhost:5000/model/predict')
    c.setopt(pycurl.HTTPHEADER, ['Accept:application/json', 'Content-Type: multipart/form-data'])
    c.setopt(pycurl.HTTPPOST, [('image', (pycurl.FORM_FILE, "assets/surfing.jpg"))])
    c.setopt(pycurl.WRITEFUNCTION, b.write)
    c.perform()
    assert c.getinfo(pycurl.RESPONSE_CODE) == 200
    c.close()

    response = b.getvalue()
    response = json.loads(response)

    assert response['status'] == 'ok'
    assert response['predictions'][0]['caption'] == 'a man riding a wave on top of a surfboard .'


if __name__ == '__main__':
    pytest.main([__file__])
