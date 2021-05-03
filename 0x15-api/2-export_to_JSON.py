#!/usr/bin/python3
""" API project """
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    employee = user.json()
    username = employee.get('username')

    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                        .format(id))
    todos = todo.json()

    filename = id + '.json'
    with open(filename, mode='w') as f:
        data = {}
        data[id] = []
        for task in todos:
            data[id].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            })
        json.dump(data, f)
