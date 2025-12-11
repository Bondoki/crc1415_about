import pytest
from fastapi.testclient import TestClient


def test_importing_api():
    # this will raise an exception if pydantic model validation fails for the api
    from crc1415_about.apis import crc1415_about_footer_pages

    assert crc1415_about_footer_pages.name == 'crc1415_about'

HTTP_OK = 200

@pytest.mark.skip(reason='Skipping static files serving test temporarily')
def test_static_files_serving():
    from crc1415_about.apis import crc1415_about_footer_pages

    app = crc1415_about_footer_pages.load()
    client = TestClient(app)
    response = client.get('/static/terms.html')
    assert response.status_code == HTTP_OK
