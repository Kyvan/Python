#!/home/kyvan/python_env/bin/python


import json
import sys
from base64 import b64encode

import requests
import urllib3

# Configuration
protocol = 'https'
host = 'wazuh'
port = '55000'
user = 'wazuh-wui'
password = 'Reproduction38Assignment?'


def error_exit(error_message):
    print(error_message)
    sys.exit(1)


# Disable insecure https warnings (for self-signed SSL certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Functions
def get_response(request_method, url, headers, verify=False, body=None):
    """Get API result"""
    if body is None:
        body = {}

    request_result = getattr(requests, request_method.lower())(url, headers=headers, verify=verify, data=body)

    if request_result.status_code == 200:
        return json.loads(request_result.content.decode())
    else:
        raise Exception(f"Error obtaining response: {request_result.json()}")

# Variables
base_url = f"{protocol}://{host}:{port}"
login_url = f"{base_url}/security/user/authenticate"
basic_auth = f"{user}:{password}".encode()
headers = {
           'Authorization': f'Basic {b64encode(basic_auth).decode()}',
           'Content-Type': 'application/json'
           }
headers['Authorization'] = f'Bearer {get_response("POST", login_url, headers)["data"]["token"]}'

# Request
def response(user_input):
    if user_input.lower() == 'get':
        endpoint = '/agents?status=active'
        my_response = get_response("GET", url=base_url + endpoint, headers=headers)
        return my_response
    elif user_input.lower() == 'post':
        raise Exception("Currently being worked on!!")
    elif user_input.lower() == 'delete':
        endpoint = '/agents?older_than=15d&agents_list=all&status=disconnected'
        my_response = get_response("DELETE", url=base_url + endpoint, headers=headers)
        return my_response
    else:
        raise Exception(f"Error obtaining response: {user_input}")

# WORK WITH THE RESPONSE AS YOU LIKE
try:
    if sys.argv[1].isalpha():
        if sys.argv[1] == 'get' or sys.argv[1] == 'post' or sys.argv[1] == 'delete':
            print(json.dumps(response(sys.argv[1]), indent=4, sort_keys=True))
        else:
            error_exit("Need to use Either POST, GET,  or DELETE")
    else:
        error_exit("Answer needs to be a string!")
except IndexError:
    error_exit("Answer needs to be a string!")
