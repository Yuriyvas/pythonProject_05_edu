import requests
import pytest
import time

base_url = 'https://www.mail.ru/'
HTTP_code = 200
url = 'https://playground.learnqa.ru/api/'

def test_get_all_posts():
    response = requests.get(f'{base_url}posts')
    assert response.status_code == HTTP_code, 'wrong status code'
    print(response.json())
    # assert len(response.json()) == 100, 'actual length does not match to expected'