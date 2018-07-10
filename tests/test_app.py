import falcon
from falcon import testing
import msgpack
import pytest

from dashtat import app


@pytest.fixture
def client():
    return testing.TestClient(app)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_list_images(client):
    response = client.simulate_get('/pulls')
    result_doc = msgpack.unpackb(response.content, encoding='utf-8')

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK
