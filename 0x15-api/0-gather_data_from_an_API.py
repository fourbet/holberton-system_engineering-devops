#!/usr/bin/python3
""" API project """
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id))
    employee = user.json()
    name = employee.get('name')

    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                        .format(id))
    todos = todo.json()
    taskDone = 0
    taskTotal = 0
    for task in todos:
        taskTotal += 1
        if task.get('completed') is True:
            taskDone += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, taskDone, taskTotal))

    for task in todos:
        if task.get('completed') is True:
            print("\t " + task.get('title'))
