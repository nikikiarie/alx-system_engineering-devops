#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

from sys import argv
import re
import requests

REST_URL = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(argv) > 1:
        if re.fullmatch(r'\d+', argv[1]):
            idq = int(argv[1])
            reqs = requests.get('{}/users/{}'.format(REST_URL, idq)).json()
            req_task = requests.get('{}/todos'.format(REST_URL)).json()
            name_req = reqs.get('name')
            tasks = list(filter(lambda i: i.get('userId') == idq, req_task))
            tasks_compl = list(filter(lambda i: i.get('completed'), tasks))
            print(
                    'Employee {} is done with tasks({}/{}):'.format(
                        name_req, len(tasks_compl),
                        len(tasks)
                        )
                    )
            if len(tasks_compl) > 0:
                for i in tasks_compl:
                    print('\t {}'.format(i.get('title')))
