#!/usr/bin/python3
"""REST API to access employees todo lists"""

import requests
import sys


if __name__ == '__main__':
    emp_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    userurl = baseUrl + "/" + emp_Id

    response = requests.get(userurl)
    employeeName = response.json().get('name')

    todoUrl = userurl + "/todos"
    response = requests.get(todoUrl)
    taskslist = response.json()
    done = 0
    done_tasks = []

    for task in taskslist:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(taskslist)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
