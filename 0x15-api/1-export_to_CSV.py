#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    emp_Id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + emp_Id

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(emp_Id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(emp_Id, username, task.get('completed'),
                               task.get('title')))
