#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    emp_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    userurl = baseUrl + "/" + emp_Id

    response = requests.get(userurl)
    username = response.json().get('username')

    todoUrl = userurl + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json

    with open('{}.csv'.format(emp_Id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(emp_Id, username, task.get('completed'),
                               task.get('title')))
