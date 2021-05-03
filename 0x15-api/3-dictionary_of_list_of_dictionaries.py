#!/usr/bin/python3
""" API project """
import requests
import sys
import json

if __name__ == "__main__":

    for id in range(1, 10):
        user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(id))
        employee = user.json()
        username = employee.get('username')

        todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                            .format(id))
        todos = todo.json()

        dict = {}
        filename = 'todo_all_employees' + '.json'
        with open(filename, mode='a') as f:
            data = []
            for task in todos:
                data.append({
                    'task': task.get('title'),
                    'completed': task.get('completed'),
                    'username': username
                })
            dict[id] = data

    with open(filename, mode='a') as f:
        json.dump(dict, f)
