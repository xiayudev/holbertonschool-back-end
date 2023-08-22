#!/usr/bin/python3
"""Module to interact with an api"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"  # base url

if __name__ == "__main__":
    response_todos = requests.get(f"{url}/todos?userId={sys.argv[1]}")
    response_users = requests.get(f"{url}/users/{sys.argv[1]}")

    todos = response_todos.json()
    user = response_users.json()

    filter_todos = {
        user.get('id'): [{
            k: v for k, v in todo.items()
            if k != 'id' and k != 'userId'} for todo in todos]}
    get_value = filter_todos[user.get('id')]

    for value in get_value:
        value['username'] = user.get('username')
        value['task'] = value['title']
        del value['title']

    with open(f"{user.get('id')}.json", mode='w') as file:
        file.write(json.dumps(filter_todos))
