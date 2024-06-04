#!/usr/bin/python3
"""
Uses a REST API to retrieve information about
an employee's TODO list progress, and exports the data in JSON format.
"""
from sys import argv
import json
import requests


if __name__ == "__main__":
    employee_id = int(argv[1])
    base_url = 'https://jsonplaceholder.typicode.com/'
    # Fetch employee data
    user_response = requests.get(f"{base_url}users/{employee_id}")
    user_data = user_response.json()
    # Fetch TODO list data
    todos_response = requests.get(f"{base_url}todos?userId={employee_id}")
    todos_data = todos_response.json()

    username = user_data.get('username')
    # Dictionary
    tasks = []
    for task in todos_data:
        tasks.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        })

    data = {employee_id: tasks}

    # JSON filename
    filename = f"{employee_id}.json"

    # Write to JSON
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile)
