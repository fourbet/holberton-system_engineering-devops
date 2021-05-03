#!/usr/bin/python3
""" API project """
import json
import requests
import sys


if __name__ == "__main__":

    dict = {}
    for id in range(1, 11):
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(id))
        employee = user.json()
        username = employee.get('username')

        todo = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos"
            .format(id))
        todos = todo.json()

        filename = 'todo_all_employees' + '.json'
        data = []
        for task in todos:
            data.append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            })
        dict[id] = data

    with open(filename, mode='w') as f:
        json.dump(dict, f)
