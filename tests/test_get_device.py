from . import test_client


test_headers = {"Device-Token": "HelloTests"}
first_responce = None


def test_get_device():
    response = test_client.get('/api/v1/get-test', headers=test_headers)
    assert response.status_code == 200
    global first_response
    first_responce = response.json()
    test_result = first_responce['message'][0]
    assert "button_color" in list(test_result.keys())
    assert "price" in list(test_result.keys())


def test_permanent_values():
    response = test_client.get('/api/v1/get-test', headers=test_headers)
    second_responce = response.json()
    test_result = second_responce['message'][0]
    assert first_responce == second_responce
