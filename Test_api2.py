import requests
import pytest
import time

base_url = 'https://jsonplaceholder.typicode.com/'
HTTP_code = 200
url = 'https://playground.learnqa.ru/api/'

def test_get_all_posts():
    response = requests.get(f'{base_url}posts')
    assert response.status_code == HTTP_code, 'wrong status code'
    print(response.json())
    assert len(response.json()) == 100, 'actual length does not match to expected'

def test_get_post1():
    response = requests.get(f'{base_url}posts/1')
    assert response.status_code == HTTP_code, 'wrong status code'
    response_data = response.json()
    expected_keys = ['userId', 'id', 'title', 'body']
    for key in response_data.keys():
        assert key in expected_keys, 'wrong keys'