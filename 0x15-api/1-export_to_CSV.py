#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    user = argv[1]
    rest_url = 'https://jsonplaceholder.typicode.com/users/' + user
    resp = requests.get(rest_url)
    name = resp.json().get('username')
    tsk = rest_url + '/todos'
    resp = requests.get(tsk)
    tsks = resp.json()

    with open('{}.csv'.format(user), 'w') as file:
        for i in tsks:
            compl = i.get('completed')
            title = i.get('title')
            file.write('"{}","{}","{}","{}"\n'.format(
                    user, name, compl, title))
