# example_module.py
# Note: This example assumes you have the 'requests' package installed. You can install it with 'pip install requests'.

import requests

def get_example_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()['title']