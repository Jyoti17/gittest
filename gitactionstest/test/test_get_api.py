import requests
import json
import pytest

base_url = "https://reqres.in/api/users?page=2"


@pytest.mark.tcid011
def test_get_method():
    response = requests.get(base_url)
    response.json()
    json_data=json.dumps((response.json()), indent=4)
    print(json_data)
    print("Test Jyoti G code")
    print("Test Yogesh Gondhali's code")


test_get_method()