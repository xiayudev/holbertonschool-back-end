#!/usr/bin/python3
"""Module to interact with an api"""
import csv
import requests
import sys

url = "https://jsonplaceholder.typicode.com"  # base url

if __name__ == "__main__":
    response_todos = requests.get(f"{url}/todos?userId={sys.argv[1]}")
    response_users = requests.get(f"{url}/users/{sys.argv[1]}")

    todos = response_todos.json()
    user = response_users.json()

    with open(f"{user.get('id')}.csv", mode='w') as file:
        write = csv.writer(file, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in todos:
            write.writerow([user.get('id'), user.get('username'),
                           todo.get('completed'), todo.get('title')])
