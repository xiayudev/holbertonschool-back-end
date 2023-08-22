#!/usr/bin/python3
"""Module to interact with an api"""
import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"  # base url

if __name__ == "__main__":
    response_todos = requests.get(f"{url}/todos")
    response_users = requests.get(f"{url}/users")

    todos = response_todos.json()
    users = response_users.json()

    filter_todos = {
        user.get('id'): [{
            k: v for k, v in todo.items() if k != 'id'}
            for todo in todos
            if todo.get('userId') == user.get('id')]
        for user in users}

    for values in filter_todos.values():
        for todos in values:
            todos['task'] = todos.get('title')
            del todos["title"]
            for user in users:
                if user.get('id') == todos.get('userId'):
                    todos['username'] = user.get('username')
                    del todos['userId']

    with open("todo_all_employees.json", mode='w') as file:
        file.write(json.dumps(filter_todos))
