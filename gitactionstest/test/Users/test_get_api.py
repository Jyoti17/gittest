import requests
import json
import pytest
import logging as logger

base_url = "https://reqres.in/api/users?page=2"


@pytest.mark.smoke
@pytest.mark.tc01
def test_get_method():
    logger.debug("Get the user data")
    response = requests.get(base_url)
    response.json()
    json_data = json.dumps((response.json()), indent=4)
    print(json_data)
    assert response.status_code == 200, f"Status code showing wrong"


@pytest.mark.smoke
@pytest.mark.tc02
def test_get_new_method():
    logger.debug("Get the user data")
    response = requests.get(base_url)
    json_data = json.dumps((response.json()), indent=4)
    assert response.status_code == 200, f"Status code showing wrong"
    print("Success")