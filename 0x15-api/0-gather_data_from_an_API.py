#!/usr/bin/python3
"""
Uses a REST API to retrieve informantion about
an employee's TODO list progress.
"""
from sys import argv
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
    # Prepare for printing
    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = []
    for todo in todos_data:
        if todo.get('completed'):
            done_tasks.append(todo)
    # Printing data
    print(f"Employee {employee_name} is done with\
          tasks({len(done_tasks)}/{total_tasks}): ")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
