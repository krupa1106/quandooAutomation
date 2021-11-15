import json

import jsonpath
import requests
import pytest


# verifying the response from the list of users
@pytest.mark.get_list_users
def test_get_list_users():
    url_get_list_users='https://reqres.in/api/users?page=2'
    response = requests.get(url_get_list_users)
    print(response)
    print(response.content)


# Verifying the get request with single user
@pytest.mark.get_single_user
def test_get_single_user():
    url_get_single_user= 'https://reqres.in/api/users/2'
    response = requests.get(url_get_single_user)
    print(response.content)
    # parsing the response to json format
    json_response = response.json()
    print(json_response)
    # fetching each data from Json
    user_id = json_response["data"]["id"]
    print(user_id)
    user_email = json_response["data"]["email"]
    print(user_email)
    user_first_name = json_response["data"]["first_name"]
    print(user_first_name)
    user_last_name = json_response["data"]["last_name"]
    print(user_last_name)
    user_avatar = json_response["data"]["avatar"]
    print(user_avatar)
    user_url = json_response["support"]["url"]
    print(user_url)




