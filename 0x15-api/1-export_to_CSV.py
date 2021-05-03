#!/usr/bin/python3
""" API project """
import csv
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

    filename = id + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([id, username, task.get('completed'),
                             task.get('title')])
