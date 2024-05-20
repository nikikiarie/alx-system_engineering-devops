#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    reqSes = requests.Session()
    emp_id = sys.argv[1]
    urlid = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            emp_id)
    url_n = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    empl = reqSes.get(urlid)
    name_empl = reqSes.get(url_n)
    empl_json = empl.json()
    user = name_empl.json()['username']
    tasks = []
    user_new = {}
    for emp in empl_json:
        tasks.append(
            {
                "task": emp.get('title'),
                "completed": emp.get('completed'),
                "username": user,
            })
    user_new[emp_id] = tasks
    file_n = emp_id + ".json"
    with open(file_n, 'w') as f:
        json.dump(user_new, f)
