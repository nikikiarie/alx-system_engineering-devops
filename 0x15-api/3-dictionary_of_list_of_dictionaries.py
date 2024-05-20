#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format
"""

import json
import requests
import sys


if __name__ == '__main__':
    rest_url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(rest_url)
    res_json = res.json()

    users_info = {}
    for i in res_json:
        id_user = i.get('id')
        user_name = i.get('username')
        rest_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
                id_user)
        rest_url = rest_url + '/todos/'
        res = requests.get(rest_url)

        tasks = res.json()
        users_info[id_user] = []
        for j in tasks:
            compl = j.get('completed')
            title = j.get('title')
            users_info[id_user].append({
                "username": user_name,
                "task": title,
                "completed": compl,
            })
            """A little Something"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_info, f)
